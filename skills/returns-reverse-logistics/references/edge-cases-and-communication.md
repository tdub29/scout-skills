# Edge Cases and Communication Patterns

## Key Edge Cases

These are situations where standard workflows fail. Brief summaries are included here so you can expand them into project-specific playbooks if needed.

1. **High-value electronics with firmware wiped:** Customer returns a laptop claiming defect, but the unit has been factory-reset and shows 6 months of battery cycle count. The device was used extensively and is now being returned as "defective" â€” grading must look beyond the clean software state.

2. **Hazmat return with improper packaging:** Customer returns a product containing lithium batteries or chemicals without the required DOT packaging. Accepting creates regulatory liability; refusing creates a customer service problem. The product cannot go back through standard parcel return shipping.

3. **Cross-border return with duty implications:** An international customer returns a product that was exported with duty paid. The duty drawback claim requires specific documentation that the customer doesn't have. The return shipping cost may exceed the product value.

4. **Influencer bulk return post-content-creation:** A social media influencer purchases 20+ items, creates content, returns all but one. Technically within policy, but the brand value was extracted. Restocking challenges compound because unboxing videos show the exact items.

5. **Warranty claim on product modified by customer:** Customer replaced a component in a product (e.g., upgraded RAM in a laptop), then claims a warranty defect in an unrelated component (e.g., screen failure). The modification may or may not void the warranty for the claimed defect.

6. **Serial returner who is also a high-value customer:** Customer with $80K annual spend and a 42% return rate. Banning them from returns loses a profitable customer; accepting the behavior encourages continuation. Requires nuanced segmentation beyond simple return rate.

7. **Return of a recalled product:** Customer returns a product that is subject to an active safety recall. The standard return process is wrong â€” recalled products follow the recall programme, not the returns programme. Mixing them creates liability and reporting errors.

8. **Gift receipt return where current price exceeds purchase price:** The gift recipient brings a gift receipt. The item is now selling for $30 more than the gift-giver paid. Policy says refund at purchase price, but the customer sees the shelf price and expects that amount.

## Communication Patterns

### Tone Calibration

- **Standard refund confirmation:** Warm, efficient. Lead with the resolution amount and timeline, not the process.
- **Denial of return:** Empathetic but clear. Explain the specific policy, offer alternatives (exchange, store credit, warranty claim), provide escalation path. Never leave the customer with no options.
- **Fraud investigation hold:** Neutral, factual. "We need additional time to process your return" â€” never say "fraud" or "investigation" to the customer. Provide a timeline. Internal communications are where you document the fraud indicators.
- **Restocking fee explanation:** Transparent. Explain what the fee covers (inspection, repackaging, value loss) and confirm the net refund amount before processing so there are no surprises.
- **Vendor RTV claim:** Professional, evidence-based. Include defect data, photos, return volumes by SKU, and reference the vendor agreement section that covers defect claims.

### Key Templates

Brief templates appear below. Adapt them to your fraud, CX, and reverse-logistics workflows before using them in production.

**RMA approval:** Subject: `Return Approved â€” Order #{order_id}`. Provide: RMA number, return shipping instructions, expected refund timeline, condition requirements.

**Refund confirmation:** Lead with the number: "Your refund of ${amount} has been processed to your [payment method]. Please allow [X] business days."

**Fraud hold notice:** "Your return is being reviewed by our processing team. We expect to have an update within [X] business days. We appreciate your patience."

