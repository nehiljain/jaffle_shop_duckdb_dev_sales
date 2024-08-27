## Online Pharmacy Use Case Description

**Business**: An online pharmacy providing prescription and over-the-counter medications with home delivery.

**Data**:

- `raw_customers`: Contains customer information including name, contact details, and address.
- `raw_prescriptions`: Tracks prescriptions, including medication name, dosage, and doctor’s approval.
- `raw_orders`: Logs customer orders, including order date, medication details, and order status.
- `raw_payments`: Records payment details, including payment method, amount, and transaction date.
- `raw_inventory`: Manages medication stock levels, including batch numbers, expiration dates, and quantities.
- `raw_shipments`: Tracks shipments, including courier details, shipment status, and delivery confirmation.

**Focus**:

- **Prescription Validation**: Ensure all orders for prescription medications have valid prescriptions linked.
- **Inventory Management**: Track stock levels, flag low inventory, and ensure medications are not expired.
- **Order Fulfillment**: Monitor order status, from placement to delivery, ensuring timely shipment.
- **Customer Segmentation**: Analyze customer purchasing patterns to identify frequent buyers and medication trends.
- **Compliance Monitoring**: Ensure data follows regulatory requirements (e.g., HIPAA) by tracking and validating prescriptions and customer information securely.

**Assumptions**:

- **Simplicity**: Focus on a single country’s regulatory environment to minimize compliance complexity.
- **Order Frequency**: Assumes customers refill prescriptions on a monthly basis, with occasional ad-hoc orders.
- **Medication Variety**: Limited to a basic selection of common prescription and OTC medications for simplicity.
- **Shipping Constraints**: Assumes standard shipping methods with no same-day delivery, to reduce complexity in shipment tracking.
- **Payment Methods**: Limited to credit cards and digital wallets to simplify payment processing.
