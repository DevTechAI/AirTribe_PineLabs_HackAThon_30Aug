---
title: "Process Payment Wallet"
slug: "process-payment-wallet-1"
excerpt: "Use the below endpoint to Process Payment Wallet."
hidden: true
createdAt: "Fri Feb 04 2022 08:22:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:50:41 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "wallet_code\\*",
    "0-1": "string",
    "0-2": "wallet_code is the unique identifier of the wallet on which the wallet transaction is intended. wallet_code can be taken from the codes table.",
    "1-0": "mobile_number",
    "1-1": "string  \n(Length = 20 Characters)",
    "1-2": "Mobile number of the customer",
    "2-0": "country_code",
    "2-1": "string  \n(Length = 10 Characters)",
    "2-2": "The country code of the mobile number of the customer. Country code for India is 91.",
    "3-0": "mobile_number",
    "3-1": "string  \n(Length = 20 Characters)",
    "3-2": "Mobile number of the customer",
    "4-0": "email_id",
    "4-1": "string  \n(Length = 100 Characters)",
    "4-2": "Email id of the cusotmer."
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Request Body payload:** 

```json JSON
{
    "wallet_data": {
        "wallet_code": "phonepe",
        "mobile_number": "9121004027"
    },
    "customer_data": {
        "country_code": "91",
        "mobile_number": "9121004027",
        "email_id": "test_customer@abc.com"
    }
}
```

**Response Payload:** 

```json 200 Success
{
    "content": "&lt;!doctype html&gt;\n&lt;html style=&quot;height:100%;width:100%;&quot;&gt;\n&lt;head&gt;\n&lt;title&gt;Processing, Please Wait...&lt;/title&gt;\n&lt;meta http-equiv=&quot;X-UA-Compatible&quot; content=&quot;IE=edge&quot;&gt;\n&lt;meta charset=&quot;utf-8&quot;&gt;\n&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;\n&lt;meta name=&quot;theme-color&quot; content=&quot;#3594E2&quot;&gt;\n&lt;script&gt;\ntry{\n  var payment_id = &quot;pay_Ix0KPLrd0HzAHf&quot;;\n  if (typeof(CheckoutBridge) !== &#39;undefined&#39; &amp;&amp; typeof(CheckoutBridge.setPaymentID) === &#39;function&#39;) {\n    CheckoutBridge.setPaymentID(payment_id);\n  } else if(window.opener){\n  opener.setPaymentID(payment_id);\n  }\n} catch(e){}\n&lt;/script&gt;\n&lt;script&gt;\n  var events = {\n    page: &#39;gateway_postform&#39;,\n    props: {\n          payment_id: &#39;pay_Ix0KPLrd0HzAHf&#39;,\n              merchant_id: &#39;DcIpvz549ymVaY&#39;,\n        },\n    load: true,\n    unload: true\n  }\n&lt;/script&gt;\n&lt;script&gt;\n!function(e){e.track=Boolean;try{if(/razorpay\\.in$/.test(location.origin))return;if(&quot;object&quot;!=typeof e.events)return;var n=e.events.props;if(0===Object.keys(n).length)return;var t,o=e.events,r=o.page,a=o.load,s=o.unload,i=o.error,c=&quot;https://lumberjack.razorpay.com/v1/track&quot;,u=&quot;MC40OTMwNzgyMDM3MDgwNjI3Nw9YnGzW&quot;,p=&quot;function&quot;==typeof navigator.sendBeacon,d=Date.now(),f=[{name:&quot;ua_parser&quot;,input_key:&quot;user_agent&quot;,output_key:&quot;user_agent_parsed&quot;}];function l(e,o){(o=o||{}).beacon=p,o.time_since_render=Date.now()-d,o.url=location.href,function(e,n){if(e&amp;&amp;n)Object.keys(n).forEach(function(t){e[t]=n[t]})}(o,n);var a={addons:f,events:[{event:r+&quot;:&quot;+e,properties:o,timestamp:Date.now()}]},s=encodeURIComponent(btoa(unescape(encodeURIComponent(JSON.stringify(a))))),i=JSON.stringify({key:u,data:s});p?navigator.sendBeacon(c,i):((t=new XMLHttpRequest).open(&quot;post&quot;,c,!0),t.send(i))}a&amp;&amp;l(&quot;load&quot;),s&amp;&amp;e.addEventListener(&quot;unload&quot;,function(){l(&quot;unload&quot;)}),i&amp;&amp;e.addEventListener(&quot;error&quot;,function(e){l(&quot;error&quot;,{message:e.message,line:e.line,col:e.col,stack:e.error&amp;&amp;e.error.stack})})}catch(e){}e.track=l}(window);\n&lt;/script&gt;\n\n&lt;style&gt;\n*{\n  box-sizing:border-box;\n  margin:0;\n  padding:0;\n}\n\nbody{\n  background:#f5f5f5;\n  overflow:hidden;\n  text-align:center;\n  height:100%;\n  white-space:nowrap;\n  margin:0;\n  padding:0;\n  font-family:-apple-system, BlinkMacSystemFont,ubuntu,verdana,helvetica,sans-serif;\n}\n\n#bg {\n  position:absolute;\n  bottom:50%;\n  width:100%;\n  height:50%;\n  background:#3594E2;\n  margin-bottom:90px;\n}\n#cntnt {\n  position:relative;\n  width:100%;\n  vertical-align: middle;\n  display: inline-block;\n  margin: auto;\n  max-width:420px;\n  min-width:280px;\n  height:95%;\n  max-height:360px;\n  background:#fff;\n  z-index:9999;\n  box-shadow:0 0 20px 0 rgba(0,0,0,0.16);\n  border-radius:4px;\n  overflow:hidden;\n  padding:24px;\n  box-sizing:border-box;\n  text-align:left;\n}\n#ftr {\n  position:absolute;\n  left:0;\n  right:0;\n  bottom:0;\n  height:80px;\n  background:#f5f5f5;\n  text-align:center;\n  color:#212121;\n  font-size:14px;\n  letter-spacing:-0.3px;\n  }\n\n#ldr {\n  width:100%;\n  height:3px;\n  position:relative;\n  margin-top:16px;\n  border-radius:3px;\n  overflow:hidden;\n}\n\n#ldr::before, #ldr::after {\n  content:&#39;&#39;;\n  position:absolute;\n  top:0;\n  bottom:0;\n  width:100%;\n}\n\n#ldr::before {\n  top:1px;\n  border-top:1px solid #bcbcbc;\n}\n\n#ldr::after {\n  background:#3594E2;\n  width:0%;\n  transition:20s cubic-bezier(0,0.1,0,1);\n}\n\n.loaded #ldr::after {\n  width:90%;\n}\n\n#logo {\n  width:48px;\n  height:48px;\n  padding:8px;\n  border:1px solid #e5e5e5;\n  border-radius:3px;\n  text-align:center;\n}\n\n#hdr {\n  min-height:48px;\n  position:relative;\n}\n\n#logo, #name, #amt {\n  display:inline-block;\n  vertical-align:middle;\n  letter-spacing:-0.5px;\n}\n\n#amt {\n  position:absolute;\n  right:0;\n  top:0;\n  background:#fff;\n  color:#212121;\n}\n\n#name {\n  line-height:48px;\n  margin-left:12px;\n  font-size:16px;\n  max-width:140px;\n  overflow:hidden;\n  text-overflow:ellipsis;\n  color:#212121;\n}\n\n#logo+#name{\n  line-height:20px;\n}\n\n#txt {\n  height:200px;\n  text-align:center;\n}\n\n#title {\n  font-size:20px;\n  line-height:24px;\n  margin-bottom:8px;\n  letter-spacing:-0.3px;\n}\n\n#msg, #cncl {\n  font-size:14px;\n  line-height:20px;\n  color:#757575;\n  margin-bottom:8px;\n  letter-spacing:-0.3px;\n}\n\n#cncl {\n  text-decoration:underline;\n  cursor:pointer;\n}\n\n#logo img {\n  max-width:100%;\n  max-height:100%;\n  vertical-align:middle;\n}\n\n@media (max-height:580px), (max-width:420px) {\n  #bg{\n     display:none;\n  }\n  body {\n    background:#3594E2;\n  }\n}\n\n@media (max-width:420px){\n  #cntnt {\n    padding:16px;\n    width:95%;\n  }\n  #name {\n    margin-left:8px;\n  }\n}\n&lt;/style&gt;\n&lt;/head&gt;\n&lt;body onload=&quot;document.form1.submit()&quot;&gt;\n  &lt;div id=&#39;bg&#39;&gt;&lt;/div&gt;\n  &lt;div style=&quot;display:inline-block;vertical-align:middle;height:100%&quot;&gt;&lt;/div&gt;\n  &lt;div id=&#39;cntnt&#39;&gt;\n    &lt;div id=&quot;hdr&quot;&gt;\n            &lt;div id=&#39;name&#39;&gt;\n                  Test\n              &lt;/div&gt;\n              &lt;div id=&quot;amt&quot;&gt;\n          &lt;div style=&quot;font-size:12px;color:#757575;line-height:15px;margin-bottom:5px;text-align:right&quot;&gt;PAYING&lt;/div&gt;\n          &lt;div style=&quot;font-size:20px;line-height:24px;&quot;&gt;&amp;#8377; 5&lt;/div&gt;\n        &lt;/div&gt;\n          &lt;/div&gt;\n    &lt;div id=&quot;ldr&quot;&gt;&lt;/div&gt;\n    &lt;div id=&quot;txt&quot;&gt;\n      &lt;div style=&quot;display:inline-block;vertical-align:middle;white-space:normal;&quot;&gt;\n        &lt;h2 id=&#39;title&#39;&gt;Loading Bank page&amp;#x2026;&lt;/h2&gt;\n        &lt;p id=&#39;msg&#39;&gt;Please wait while we redirect you to your Bank page&lt;/p&gt;\n      &lt;/div&gt;\n      &lt;div style=&quot;display:inline-block;vertical-align:middle;height:100%&quot;&gt;&lt;/div&gt;\n    &lt;/div&gt;\n    &lt;div id=&#39;ftr&#39;&gt;\n      &lt;div style=&quot;display:inline-block;&quot;&gt;Secured by &lt;img style=&quot;vertical-align:middle;margin-bottom:5px;&quot; height=&quot;20px&quot; src=https://dashboard-activation.s3.amazonaws.com/org_100000razorpay/checkout_logo/phpgGkcfA&gt;&lt;/div&gt;\n      &lt;div style=&quot;display:inline-block;vertical-align:middle;height:100%&quot;&gt;&lt;/div&gt;\n    &lt;/div&gt;\n  &lt;/div&gt;\n  &lt;form id=&quot;form1&quot; name=&quot;form1&quot; action=&quot;https://api.razorpay.com/v1/gateway/mocksharp/payment?key_id=rzp_test_i00i1DaqSdP1bj&quot; method=&quot;post&quot; onsubmit=&quot;return true;&quot;&gt;\n      &lt;input type=&quot;hidden&quot; name=&quot;action&quot; value=&quot;authorize&quot;&gt;\n      &lt;input type=&quot;hidden&quot; name=&quot;amount&quot; value=&quot;500&quot;&gt;\n      &lt;input type=&quot;hidden&quot; name=&quot;method&quot; value=&quot;wallet&quot;&gt;\n      &lt;input type=&quot;hidden&quot; name=&quot;payment_id&quot; value=&quot;Ix0KPLrd0HzAHf&quot;&gt;\n      &lt;input type=&quot;hidden&quot; name=&quot;callback_url&quot; value=&quot;https://api.razorpay.com/v1/payments/pay_Ix0KPLrd0HzAHf/callback/b336ff52cc5daf051414a4ea8dbe8d4b2d07a3e4/rzp_test_i00i1DaqSdP1bj&quot;&gt;\n      &lt;input type=&quot;hidden&quot; name=&quot;recurring&quot; value=&quot;0&quot;&gt;\n    &lt;/form&gt;\n  &lt;form id=&quot;form2&quot; name=&quot;form2&quot;&gt;\n    &lt;input type=&quot;hidden&quot; name=&quot;type&quot; value=&quot;first&quot;&gt;\n    &lt;input type=&quot;hidden&quot; name=&quot;gateway&quot; value=&quot;eyJpdiI6IjVFbjJXWWRyTk03aWhOekYwZHlRU0E9PSIsInZhbHVlIjoic2syQjFrYlZHTzNDRFwvTDR6TXZQSkxtVm5XakxZMEdcLzNVRHRuTXUrNjJvPSIsIm1hYyI6IjYzNjI1MTQ4ODE0MjczNThhZjE2ODQxNzBkNjEwYzRiNjNkMWY1OGFhOTQ1YWU1ZTFmYzBjOGUyYjUzYjY5ZjYifQ==&quot;&gt;\n  &lt;/form&gt;\n  &lt;script&gt;\n    setTimeout(function() {\n      document.body.className = &#39;loaded&#39;;\n    }, 10);\n\n    setTimeout(function(){\n      document.getElementById(&#39;title&#39;).innerHTML = &#39;Still trying to load...&#39;;\n      document.getElementById(&#39;msg&#39;).innerHTML = &#39;The bank page is taking time to load.&#39;;\n    }, 10000);\n  &lt;/script&gt;\n&lt;/body&gt;\n&lt;/html&gt;\n",
    "payment_id": 1014397,
    "order_id": 34594,
    "amount_in_paise": 500,
    "response_code": 1,
    "response_message": "Payment Successful!"
}
```
```json 400 Bad Request
{
    "error_code": "-1",
    "error_message": "Sorry, your transaction has failed."
}
```

| Parameter Name   | Type   | Description                           |
| :--------------- | :----- | :------------------------------------ |
| content          | string | Html content to load the output data. |
| payment_id       | long   | Unique payment id.                    |
| order_id         | long   | Unique order id.                      |
| amount_in_paise  | long   | Amount paid in paise.                 |
| response_code    | string | Response code.                        |
| response_message | string | Short message about code.             |
