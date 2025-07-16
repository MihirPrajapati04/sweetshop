import streamlit as st
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.add_service import AddSweetService
from sweetshop.view_service import ViewSweetService
from sweetshop.search_service import SearchSweetService
from sweetshop.category_search_service import CategorySearchService
from sweetshop.price_search_service import PriceSearchService
from sweetshop.inventory_service import InventoryService
from sweetshop.delete_service import DeleteSweetService

# Initialize services
db = DBManager()
db.connect()

add_service = AddSweetService(db)
view_service = ViewSweetService(db)
search_service = SearchSweetService(db)
category_service = CategorySearchService(db)
price_service = PriceSearchService(db)
inventory_service = InventoryService(db)
delete_service = DeleteSweetService(db)

st.set_page_config(page_title="Sweet Shop Manager", layout="centered")

st.title("🍭 Sweet Shop Management System")

tabs = st.tabs(["➕ Add Sweet", "📋 View All", "🔍 Search", "🛒 Purchase", "📦 Restock", "🗑️ Delete"])

# 1. Add Sweet
with tabs[0]:
    st.header("➕ Add New Sweet")
    with st.form("add_form"):
        id = st.number_input("Sweet ID", min_value=1)
        name = st.text_input("Sweet Name")
        category = st.text_input("Category")
        price = st.number_input("Price", min_value=0.0, step=0.5)
        quantity = st.number_input("Quantity", min_value=1)
        submitted = st.form_submit_button("Add Sweet")

        if submitted:
            sweet = Sweet(id=id, name=name, category=category, price=price, quantity=quantity)
            try:
                add_service.add_sweet(sweet)
                st.success(f"{name} added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

# 2. View All
with tabs[1]:
    st.header("📋 All Sweets in Inventory")
    sweets = view_service.view_all_sweets()
    if sweets:
        st.table([s.__dict__ for s in sweets])
    else:
        st.info("No sweets found in inventory.")

# 3. Search
with tabs[2]:
    st.header("🔍 Search Sweets")

    search_type = st.radio("Search by:", ["Name", "Category", "Price Range"])

    if search_type == "Name":
        name = st.text_input("Enter name:")
        if st.button("Search"):
            results = search_service.search_by_name(name)
            st.table([s.__dict__ for s in results] if results else [{"Info": "No match found."}])

    elif search_type == "Category":
        category = st.text_input("Enter category:")
        if st.button("Search"):
            results = category_service.search_by_category(category)
            st.table([s.__dict__ for s in results] if results else [{"Info": "No match found."}])

    elif search_type == "Price Range":
        min_price = st.number_input("Min Price", min_value=0.0)
        max_price = st.number_input("Max Price", min_value=0.0)
        if st.button("Search"):
            results = price_service.search_by_price_range(min_price, max_price)
            st.table([s.__dict__ for s in results] if results else [{"Info": "No match found."}])

# 4. Purchase Sweet
with tabs[3]:
    st.header("🛒 Purchase Sweet")
    purchase_id = st.number_input("Sweet ID to Purchase", min_value=1, step=1)
    purchase_qty = st.number_input("Quantity to Purchase", min_value=1)
    if st.button("Purchase"):
        try:
            inventory_service.purchase_sweet(purchase_id, purchase_qty)
            st.success("Purchase successful!")
        except Exception as e:
            st.error(f"Error: {e}")

# 5. Restock Sweet
with tabs[4]:
    st.header("📦 Restock Sweet")
    restock_id = st.number_input("Sweet ID to Restock", min_value=1, step=1)
    restock_qty = st.number_input("Quantity to Add", min_value=1)
    if st.button("Restock"):
        try:
            inventory_service.restock_sweet(restock_id, restock_qty)
            st.success("Restocked successfully!")
        except Exception as e:
            st.error(f"Error: {e}")

# 6. Delete Sweet
with tabs[5]:
    st.header("🗑️ Delete Sweet")
    del_id = st.number_input("Sweet ID to Delete", min_value=1, step=1)
    if st.button("Delete"):
        try:
            delete_service.delete_sweet(del_id)
            st.success("Sweet deleted successfully!")
        except Exception as e:
            st.error(f"Error: {e}")

# Close DB connection on app stop
st.sidebar.markdown("Built with ❤️ using Streamlit")
