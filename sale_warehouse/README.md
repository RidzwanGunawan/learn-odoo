
---

## 🔁 How It Works

1. A user confirms a Sales Order in Odoo.
2. The `sale_notification` module overrides the `action_confirm()` method.
3. It sends a new record to `warehouse.notification` (from the other module).
4. Warehouse team sees the notification and marks it as done via button.

---

## 📌 Module: `warehouse_notification`

- New model: `warehouse.notification`
- Fields:
  - `order_id`
  - `customer`
  - `total`
  - `message`
  - `state` (`pending`, `done`)
- UI:
  - Tree and Form view
  - Action button: **"Tandai Selesai"**

---

## 🔔 Module: `sale_notification`

- Inherits `sale.order`
- Overrides `action_confirm()`
- On confirm, creates a new `warehouse.notification` record with order data

---

## 🛠 Installation

1. Copy both modules into your Odoo `addons_path` (same folder is fine).
2. Restart Odoo.
3. Update the app list.
4. Install both modules from the Apps menu:
   - `Warehouse Notification`
   - `Sale Notification`

---

## 📝 Example Output

When confirming a sale, the following will be created in the Warehouse Notification screen:

| Order ID | Customer | Total | Message                                      | State   |
|----------|----------|-------|----------------------------------------------|---------|
| 00459    | PT. ABC  | 1200  | Sales Order #SO00459 has been confirmed...   | Pending |

---

## 🧑‍💻 Developer Notes

- Compatible with Odoo 15, 16, 17, 18+
- Uses `self.env[...]` to cross-access models between modules
- No external dependencies

---

## 📄 License

MIT License – free to use, modify, and distribute.
