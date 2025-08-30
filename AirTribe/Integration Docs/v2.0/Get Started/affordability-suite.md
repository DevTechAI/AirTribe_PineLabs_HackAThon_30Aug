---
title: "Affordability Suite"
slug: "affordability-suite"
excerpt: "Learn how to integrate with Plural EMI APIs and offer EMI payments on the purchase."
hidden: false
createdAt: "Mon Nov 25 2024 10:28:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Feb 25 2025 09:08:41 GMT+0000 (Coordinated Universal Time)"
---
With Plural’s Affordability Suite, you can empower your customers with flexible payment options that reduce upfront costs and make high-value purchases more accessible. This feature is ideal for businesses looking to attract more customers, increase conversions, and expand into underserved markets across India, all while offering a seamless checkout experience.

With Plural you can make payments in EMIs using the below payment methods.

[block:html]
{
  "html": "<style>\n.card-container {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));\n  gap: 20px;\n  padding: 40px;\n  max-width: 1200px;\n  margin: 0 auto;\n}\n\n/* Card styling */\n.card {\n  background-color: #FBF8FD;\n  border: 1px solid #E8E8E8;\n  border-radius: 8px;\n  padding: 20px;\n  display: flex;\n  align-items: flex-start;\n  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);\n  transition: transform 0.2s ease, box-shadow 0.2s ease;\n}\n\n\n.card:hover {\n  transform: translateY(-5px);\n  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);\n}\n\n/* Icon styling */\n.card-icon {\n  margin-right: 15px;\n}\n\n.card-icon img {\n  width: 50px;\n  height: 50px;\n}\n\n/* Card content */\n.card-content h2 {\n  font-size: 1.25rem;\n  color: black;\n  margin: 0;\n}\n\n.card-content p {\n  margin: 8px 0 0;\n  color: black;\n  font-size: 0.9rem;\n}\n</style>\n<body>\n  <!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>Card Layout</title>\n  <link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n<body>\n  <div class=\"card-container\">\n    <!-- Card 1 -->\n    <div class=\"card\">\n      <div class=\"card-icon\">\n        <svg width=\"40\" height=\"40\" viewBox=\"0 0 40 40\" fill=\"none\" xmlns=\"<http://www.w3.org/2000/svg>\">\n            <rect width=\"40\" height=\"40\" rx=\"8\" fill=\"rgb(246, 229, 255)\" />\n            <path\n              d=\"M8.33301 20.0013C8.33301 15.6015 8.33301 13.4016 9.69984 12.0348C11.0667 10.668 13.2666 10.668 17.6663 10.668H22.333C26.7328 10.668 28.9327 10.668 30.2995 12.0348C31.6663 13.4016 31.6663 15.6015 31.6663 20.0013C31.6663 24.4011 31.6663 26.601 30.2995 27.9678C28.9327 29.3346 26.7328 29.3346 22.333 29.3346H17.6663C13.2666 29.3346 11.0667 29.3346 9.69984 27.9678C8.33301 26.601 8.33301 24.4011 8.33301 20.0013Z\"\n              stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" />\n            <path d=\"M17.6667 24.668H13\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n            <path d=\"M22.333 24.668H20.583\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n            <path d=\"M8.33301 17.668L31.6663 17.668\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n          </svg>\n      </div>\n      <div class=\"card-content\">\n        <h2><a href=\"https://developer.pluralonline.com/v2.0/docs/credit-card-emi\" target=\"_blank\">Credit Card EMI</a></h2>\n        <p>Enables your customers to transform high-value purchases into affordable monthly instalments using their credit cards.</p>\n      </div>\n    </div>\n    \n    <!-- Card 2 -->\n    <div class=\"card\">\n      <div class=\"card-icon\">\n        <svg width=\"40\" height=\"40\" viewBox=\"0 0 40 40\" fill=\"none\" xmlns=\"<http://www.w3.org/2000/svg>\">\n            <rect width=\"40\" height=\"40\" rx=\"8\" fill=\"rgb(246, 229, 255)\" />\n            <path\n              d=\"M8.33301 20.0013C8.33301 15.6015 8.33301 13.4016 9.69984 12.0348C11.0667 10.668 13.2666 10.668 17.6663 10.668H22.333C26.7328 10.668 28.9327 10.668 30.2995 12.0348C31.6663 13.4016 31.6663 15.6015 31.6663 20.0013C31.6663 24.4011 31.6663 26.601 30.2995 27.9678C28.9327 29.3346 26.7328 29.3346 22.333 29.3346H17.6663C13.2666 29.3346 11.0667 29.3346 9.69984 27.9678C8.33301 26.601 8.33301 24.4011 8.33301 20.0013Z\"\n              stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" />\n            <path d=\"M17.6667 24.668H13\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n            <path d=\"M22.333 24.668H20.583\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n            <path d=\"M8.33301 17.668L31.6663 17.668\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n          </svg>\n      </div>\n      <div class=\"card-content\">\n         <h2><a href=\"https://developer.pluralonline.com/v2.0/docs/debit-card-emi\" target=\"_blank\">Debit Card EMI</a></h2>\n        <p>Enables pre-approved debit cardholders to make purchases in installments, with monthly deductions directly from their savings account</p>\n      </div>\n    </div>\n    \n    <!-- Card 3 -->\n    <div class=\"card\">\n      <div class=\"card-icon\">\n       <svg width=\"40\" height=\"40\" viewBox=\"0 0 40 40\" fill=\"none\" xmlns=\"<http://www.w3.org/2000/svg>\">\n            <rect width=\"40\" height=\"40\" rx=\"8\" fill=\"rgb(246, 229, 255)\" />\n            <path\n              d=\"M8.33301 20.0013C8.33301 15.6015 8.33301 13.4016 9.69984 12.0348C11.0667 10.668 13.2666 10.668 17.6663 10.668H22.333C26.7328 10.668 28.9327 10.668 30.2995 12.0348C31.6663 13.4016 31.6663 15.6015 31.6663 20.0013C31.6663 24.4011 31.6663 26.601 30.2995 27.9678C28.9327 29.3346 26.7328 29.3346 22.333 29.3346H17.6663C13.2666 29.3346 11.0667 29.3346 9.69984 27.9678C8.33301 26.601 8.33301 24.4011 8.33301 20.0013Z\"\n              stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" />\n            <path d=\"M17.6667 24.668H13\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n            <path d=\"M22.333 24.668H20.583\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n            <path d=\"M8.33301 17.668L31.6663 17.668\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n          </svg>\n      </div>\n      <div class=\"card-content\">\n        <h2><a href=\"https://developer.pluralonline.com/v2.0/docs/cardless-emi\" target=\"_blank\">Cardless EMI</a></h2>\n        <p>Provides customers the option to avail of EMIs without a credit or debit card by using their mobile number, PAN, or other KYC details, often linked to pre-approved limits from NBFCs or lenders</p>\n      </div>\n    </div>\n    \n    <!-- Card 4 -->\n    <div class=\"card\">\n      <div class=\"card-icon\">\n        <svg width=\"40\" height=\"40\" viewBox=\"0 0 40 40\" fill=\"none\" xmlns=\"<http://www.w3.org/2000/svg>\">\n            <rect width=\"40\" height=\"40\" rx=\"8\" fill=\"rgb(246, 229, 255)\" />\n            <path\n              d=\"M8.33301 20.0013C8.33301 15.6015 8.33301 13.4016 9.69984 12.0348C11.0667 10.668 13.2666 10.668 17.6663 10.668H22.333C26.7328 10.668 28.9327 10.668 30.2995 12.0348C31.6663 13.4016 31.6663 15.6015 31.6663 20.0013V22.3346C31.6663 26.7344 31.6663 28.9343 30.2995 30.3011C28.9327 31.668 26.7328 31.668 22.333 31.668H17.6663C13.2666 31.668 11.0667 31.668 9.69984 30.3011C8.33301 28.9343 8.33301 26.7344 8.33301 22.3346V20.0013Z\"\n              stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" />\n            <path d=\"M14.167 10.668V8.91797\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n            <path d=\"M25.833 10.668V8.91797\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n            <circle cx=\"25.25\" cy=\"25.25\" r=\"1.75\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" />\n            <path d=\"M8.91675 16.5H31.0834\" stroke=\"rgb(90, 0, 131)\" stroke-width=\"1.75\" stroke-linecap=\"round\" />\n          </svg>\n      </div>\n      <div class=\"card-content\">\n        <h2><a href=\"https://developer.pluralonline.com/v2.0/docs/split-emi\" target=\"_blank\">Bullet Payment</a></h2>\n        <p>Allows customers to pay smaller monthly EMIs and settle a significant portion of the amount as a lump sum (\"bullet payment\") at the end of the tenure.</p>\n      </div>\n    </div>\n  </div>\n</body>\n</html>\n</body>\n"
}
[/block]


## EMI Categories to Suit Diverse Needs

**Bank EMI**: Flexible payment solutions through partnerships with leading banks, ensuring broad accessibility and convenience.

**Brand EMI**: Exclusive EMI offers supported by specific brands, giving your customers additional affordability on their favorite products.

## Additional Customer Benefits

**Low-Cost**: Enjoy flexible payments with no extra interest or hidden fees — pay only the product price in easy instalments. The interest charged by the issuer will be fully subsidized, with the subvention costs covered by one or more entities, such as the brand and brand partnerships.

**No-Cost**:  Enjoy flexible payments with reduced interest rates, making high-value purchases more affordable over time. A portion of the interest charged by the issuer will be subsidized, with the subvention costs shared by one or more entities, such as the brand and brand partnerships.

**Standard EMI**: Spread your payments over time with standard interest rates, providing greater flexibility for your budget. This will have no subvention and the customer is expected to bear all the interest.

**Post-Cashback and Instant Discounts**: Enhance your customer satisfaction with post-purchase cashback and instant discount options, providing immediate savings and added value.

## Payment Options Based on Cart

### 1. Single Cart EMI:

This option allows customers to purchase a single product and avail of EMI options specifically for that item.

**Key Features**:

- Ideal for smaller purchases or when financing is required for one particular product.
- The EMI is calculated based on the price of the single product only.
- Merchants or brands can fully or partially subsidize the interest (subvention) for this product.

**Use Case**: A customer buying a smartphone worth ₹20,000 can opt for EMI on just this item, making it more affordable by spreading the payment over several months.

### 2. Multi-Cart EMI:

This option enables customers to purchase multiple products in a single transaction and avail of EMI options for the combined total amount.

**Key Features**:

- Perfect for customers who want to purchase multiple items together while managing payments through instalments.
- The EMI is calculated on the total price of all the selected products.
- Interest (subvention) on each item can be fully or partially subsidized by merchants or brands.
- All products in the cart will share the same EMI tenure.

**Use Case**: A customer purchasing a washing machine, refrigerator, and microwave oven in one transaction can combine their costs (e.g., ₹60,000 total) into a single EMI plan, making it easier to afford the purchase.

### Key Difference:

- **Single Cart EMI** is for financing one item at a time.
- **Multi-Cart EMI** bundles multiple items into one EMI plan, simplifying payments for larger purchases.

These options enhance customer affordability and flexibility, helping merchants increase conversions and average order value.

## Bullet Payment EMI

The Bullet Payment EMI Program allows customers to pay smaller monthly EMIs and settle a significant portion of the amount as a lump sum ("bullet payment") at the end of the tenure.

**How It Works**:

- Customers pay low EMIs throughout the repayment tenure. (usually a no cost EMI)
- At the end of the tenure, they make a single, larger payment to close the loan.

**Benefits for Customers**:

- Lower monthly outflows make it easier to manage cash flow.
- Suitable for customers expecting a future inflow of funds (e.g., bonuses or returns).

**Benefits for Merchants**:

- Attracts customers who may delay purchases due to current financial constraints.
- Drives sales by offering affordable short-term monthly payments combined with deferred lump sum repayment.
- It also allows the user to skip the bullet payment by upgrading to newer product by the brand in the same or different EMI scheme, ensuring high AOV repeat customer for brand & merchant.

## Full Swipe Offer

A Full Swipe Offer allows your customers to pay the full transaction amount upfront using their card and later receive a cashback or discount. The funding for this offer is shared among multiple stakeholders, such as the brand, or issuing bank. Unlike EMI options, this type of offer incentivizes purchases by providing immediate financial benefits to the customer.

For example, a customer purchasing a product for ₹20,000 may receive a ₹2,000 cashback, funded collaboratively by the brand, and bank. The cashback or discount is either credited back to your customer’s account after the transaction or applied directly at checkout, based on the offer terms.

** Key Benefits**:

- Attract more customers without directly lowering product prices.
- Drive sales while distributing the cost of the offer among stakeholders, making it more sustainable.
- Seamless integration into the checkout process ensures a smooth customer experience.

These offers are managed through predefined agreements between stakeholders, ensuring clear funding responsibilities, reconciliation, and transparency. Full Swipe Offers effectively enhance customer appeal while maintaining financial balance for all involved parties.

## Tokenization:

Tokenization is a game-changing feature that enhances payment success rates, simplifies the EMI checkout process, and ensures the highest level of security for your customers.

**Tokens**: Plural supports credit and debit card transactions through tokenized processing, including guest checkouts using Alt ID tokens for added convenience.

**Network Support**: Visa and Mastercard are fully supported for both Token and Alt ID processing. However, Rupay currently does not support PAR-based loan booking.

This advanced feature ensures a seamless and secure payment experience, driving customer trust and satisfaction.

## Supported Tokens and Networks:

The table below displays the supported tokens for each card network.

| Card Network | Card Type | Transactions Supported | Tokenisation Supported | CVV-Less Supported |
| ------------ | --------- | ---------------------- | ---------------------- | ------------------ |
| Visa         | Debit     | Yes                    | Yes                    | Yes                |
| Visa         | Credit    | Yes                    | Yes                    | Yes                |
| Mastercard   | Debit     | Yes                    | Yes                    | Yes                |
| Mastercard   | Credit    | Yes                    | Yes                    | Yes                |
| Amex         | Credit    | No                     | No                     | No                 |
| Diners       | Credit    | Yes                    | No                     | No                 |
