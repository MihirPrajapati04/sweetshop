
# 🧪 Sweet Shop Management System — Test Report

**Generated:** 2025-07-16  
**Test Framework:** Python `unittest`  
**Total Tests:** 21  
**Status:** ✅ All Tests Passed Successfully

---

## ✅ Test Summary

| Module                         | Tests | Status |
|--------------------------------|--------|--------|
| `test_add_service.py`          | 5      | ✅ PASS |
| `test_view_service.py`         | 2      | ✅ PASS |
| `test_search_service.py`       | 3      | ✅ PASS |
| `test_category_search_service.py` | 2      | ✅ PASS |
| `test_price_search_service.py` | 2      | ✅ PASS |
| `test_delete_service.py`       | 2      | ✅ PASS |
| `test_inventory_service.py`    | 5      | ✅ PASS |
| **Total**                      | **21** | ✅ All PASS |

---

## 📋 Full Execution Log

```

test_add_sweet_inserts_record (tests.test_add_service.TestAddSweetService) ... ok
test_add_sweet_stores_correct_name (tests.test_add_service.TestAddSweetService) ... ok
test_add_sweet_stores_correct_category (tests.test_add_service.TestAddSweetService) ... ok
test_add_sweet_stores_correct_price (tests.test_add_service.TestAddSweetService) ... ok
test_add_sweet_stores_correct_quantity (tests.test_add_service.TestAddSweetService) ... ok

test_view_all_sweets_returns_list (tests.test_view_service.TestViewSweetService) ... ok
test_view_all_sweets_returns_empty_list_when_no_records ... ok

test_search_by_name_returns_matching_sweets ... ok
test_search_by_name_returns_empty_list_when_no_match ... ok
test_search_by_name_case_insensitive ... ok

test_category_search_case_insensitive ... ok
test_category_search_no_match ... ok

test_price_range_returns_matching_sweets ... ok
test_price_range_returns_empty_list_when_no_match ... ok

test_delete_sweet_removes_record_by_id ... ok
test_delete_sweet_does_not_fail_for_nonexistent_id ... ok

test_purchase_sweet_decreases_quantity ... ok
test_purchase_raises_error_when_stock_insufficient ... ok
test_purchase_raises_error_when_sweet_id_invalid ... ok
test_restock_sweet_increases_quantity ... ok
test_restock_sweet_raises_error_for_invalid_id ... ok
```

---

## 🕓 Final Result

```

---

Ran 21 tests in 0.354s

OK ✅ All tests passed successfully.

```

---

> ✅ This report confirms the complete functional correctness of the system using unit tests developed via **Test-Driven Development (TDD)**.




