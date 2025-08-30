---
title: "Process Payment Card"
slug: "process-payment-card-1"
excerpt: "When order creation is successful and successful response received by the merchant then the merchant needs to call second consecutive server to server call which would process the payment to create unique transction id. In this API call merchant need to pass Card/UPI/GPAY/Netbanking transaction related data."
hidden: true
createdAt: "Thu Feb 03 2022 12:12:14 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:49:57 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "card_number\\*",
    "0-1": "string  \n(Length=19 Characters)",
    "0-2": "Card number",
    "1-0": "cvv\\*",
    "1-1": "string  \n(Length=6 Characters)",
    "1-2": "CVV",
    "2-0": "card_holder  \n\\_name\\*",
    "2-1": "string  \n(Length=150 Characters)",
    "2-2": "Name on the card.",
    "3-0": "card_expiry  \n\\_year\\*",
    "3-1": "string  \n(Length=2 Characters)",
    "3-2": "The year of card expiry. For example: \"2025\"",
    "4-0": "card_expiry  \n\\_month",
    "4-1": "string  \n(Length=4 Characters)",
    "4-2": "Card expiry month. For example if the card expiry month is March then the value to be sent is \"03\"",
    "5-0": "is_card_to_  \nbe_saved",
    "5-1": "Bool",
    "5-2": "saved card details ofr future use.",
    "6-0": "customer_data",
    "6-1": "()",
    "6-2": "",
    "7-0": "mobile_no",
    "7-1": "string  \n(Length = 20 Characters)",
    "7-2": "Vaild mobile number",
    "8-0": "country_code",
    "8-1": "string  \n(Length = 10 Characters)",
    "8-2": "Vaild country code.",
    "9-0": "email_id",
    "9-1": "string  \n(Length = 105 Characters)",
    "9-2": "Email of the user.",
    "10-0": "customer_token\\*",
    "10-1": "string",
    "10-2": "Generated customer token."
  },
  "cols": 3,
  "rows": 11,
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
  "card_data": {
    "card_number": "4012001037141112",
    "cvv": "123",
    "card_holder_name": "BALWANT",
    "card_expiry_year": "2024",
    "card_expiry_month": "05",
    "is_card_to_be_saved": false
  },
  "customer_data": {
    "mobile_no": "xxx",
    "country_code": "91",//Optional If send then okay otherwise we are assigning default value
    "email_id": "balwant.singh@pinelabs.com",
    "customer_token": "vQ7ssVqGlcfEUpGdzycwnQ=="
  }
}
```

**Response Payload:** 

```json 200 Success
"content": "&lt;!doctype html>\n&lt;html>\n&lt;head>\n  &lt;title>&lt;/title>\n  &lt;meta http-equiv=&quot;X-UA-Compatible&quot; content=&quot;IE=edge&quot;>\n  &lt;meta charset=&quot;utf-8&quot; />\n  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;>\n  &lt;link href=&quot;https://fonts.googleapis.com/icon?family=Material+Icons&quot; rel=&quot;stylesheet&quot;/>\n  &lt;link href=&quot;https://fonts.googleapis.com/css?family=Muli:400,600,800&quot; rel=&quot;stylesheet&quot;/>\n&lt;/head>\n&lt;script>\n  var events = {\n    page: &#39;gateway_otp_postform&#39;,\n    props: {\n          payment_id: &#39;pay_IpBZ16y9FkPLuJ&#39;,\n              merchant_id: &#39;DcIpvz549ymVaY&#39;,\n        },\n    load: true,\n    unload: true\n  }\n&lt;/script>\n&lt;script>\n!function(e){e.track=Boolean;try{if(/razorpay\\.in$/.test(location.origin))return;if(&quot;object&quot;!=typeof e.events)return;var n=e.events.props;if(0===Object.keys(n).length)return;var t,o=e.events,r=o.page,a=o.load,s=o.unload,i=o.error,c=&quot;https://lumberjack.razorpay.com/v1/track&quot;,u=&quot;MC40OTMwNzgyMDM3MDgwNjI3Nw9YnGzW&quot;,p=&quot;function&quot;==typeof navigator.sendBeacon,d=Date.now(),f=[{name:&quot;ua_parser&quot;,input_key:&quot;user_agent&quot;,output_key:&quot;user_agent_parsed&quot;}];function l(e,o){(o=o||{}).beacon=p,o.time_since_render=Date.now()-d,o.url=location.href,function(e,n){if(e&amp;&amp;n)Object.keys(n).forEach(function(t){e[t]=n[t]})}(o,n);var a={addons:f,events:[{event:r+&quot;:&quot;+e,properties:o,timestamp:Date.now()}]},s=encodeURIComponent(btoa(unescape(encodeURIComponent(JSON.stringify(a))))),i=JSON.stringify({key:u,data:s});p?navigator.sendBeacon(c,i):((t=new XMLHttpRequest).open(&quot;post&quot;,c,!0),t.send(i))}a&amp;&amp;l(&quot;load&quot;),s&amp;&amp;e.addEventListener(&quot;unload&quot;,function(){l(&quot;unload&quot;)}),i&amp;&amp;e.addEventListener(&quot;error&quot;,function(e){l(&quot;error&quot;,{message:e.message,line:e.line,col:e.col,stack:e.error&amp;&amp;e.error.stack})})}catch(e){}e.track=l}(window);\n&lt;/script>\n\n&lt;body>\n    &lt;div id=&quot;preloading&quot;>\n        &lt;style>\n            body {\n                background: #f4f4f4;\n            }\n        &lt;/style>\n        &lt;style>\n@keyframes  lo{to{transform:rotate(360deg)}}@-webkit-keyframes lo{to{-webkit-transform:rotate(360deg)}}\n.loader{height:24px;width:24px;border-radius:50%;display:inline-block;\n  animation:lo .8s infinite linear;-webkit-animation:lo .8s infinite linear;\n  transition:0.3s;-webkit-transition:0.3s;\n  opacity:0;border:2px solid #3395FF;border-top-color:transparent}\n.vis{opacity:1}\n&lt;/style>\n&lt;div class=&quot;loader vis&quot; style=&quot;position:absolute;top:115px;left:50%;margin-left:-12px&quot;>&lt;/div>\n        &lt;img src=&quot;https://cdn.razorpay.com/logo.svg&quot; id=&quot;logo&quot; height=&quot;35px&quot; style=&quot;margin:30px auto 10px; display:block&quot;>\n    &lt;/div>\n  &lt;script type=&quot;text/javascript&quot;>\n    // input data //\n    var data = {&quot;type&quot;:&quot;otp&quot;,&quot;request&quot;:{&quot;url&quot;:&quot;https:\/\/api.razorpay.com\/v1\/payments\/pay_IpBZ16y9FkPLuJ\/otp_submit\/4f3ae8d949e9be5ce4a0c70e08b7114bc8e06dc2?key_id=rzp_test_i00i1DaqSdP1bj&quot;,&quot;content&quot;:{&quot;type&quot;:&quot;otp&quot;,&quot;bank&quot;:&quot;ICIC&quot;,&quot;next&quot;:[&quot;submit_otp&quot;,&quot;resend_otp&quot;]},&quot;method&quot;:&quot;POST&quot;},&quot;version&quot;:1,&quot;payment_id&quot;:&quot;pay_IpBZ16y9FkPLuJ&quot;,&quot;gateway&quot;:&quot;eyJpdiI6ImUrXC8zWktKRFFycUdnS04zU3pybTV3PT0iLCJ2YWx1ZSI6ImM1dlNmR2pGQ3czZlM2cnZVNEQ3bnh0NlFkUmY2STdpSmowXC9ETW9LV0dZPSIsIm1hYyI6IjlkNTVhNjU5Y2NiMzA5MTdhMTNmYjU0YmI4MjgwOGQ2NzY3OTFlYTVlOGNiZDA4NGIwMDU1NGEzZjAxMzgxZjUifQ==&quot;,&quot;contact&quot;:&quot;+919050157978&quot;,&quot;amount&quot;:&quot;5.00&quot;,&quot;formatted_amount&quot;:&quot;₹ 5&quot;,&quot;wallet&quot;:null,&quot;merchant&quot;:&quot;Test&quot;,&quot;merchant_id&quot;:&quot;DcIpvz549ymVaY&quot;,&quot;theme_color&quot;:&quot;#3594E2&quot;,&quot;nobranding&quot;:false,&quot;redirect&quot;:&quot;https:\/\/api.razorpay.com\/v1\/payments\/pay_IpBZ16y9FkPLuJ\/authentication\/redirect?key_id=rzp_test_i00i1DaqSdP1bj&quot;,&quot;metadata&quot;:{&quot;issuer&quot;:&quot;HDFC&quot;,&quot;network&quot;:&quot;VISA&quot;,&quot;last4&quot;:&quot;1112&quot;,&quot;iin&quot;:&quot;401200&quot;}};\n    // input data //\n    try { CheckoutBridge.setPaymentID(data.payment_id) } catch(e){}\n  &lt;/script>\n  &lt;div id=&quot;app&quot;>&lt;/div>\n  &lt;script type=&quot;text/javascript&quot; src=&quot;https://cdn.razorpay.com/static/otp/bundle.js&quot; charset=&quot;utf-8&quot;>&lt;/script>\n  \n  &lt;form class=&quot;card&quot; id=&quot;otpform&quot; name=&quot;otpform&quot; action=&quot;https://api.razorpay.com/v1/payments/pay_IpBZ16y9FkPLuJ/otp_submit/4f3ae8d949e9be5ce4a0c70e08b7114bc8e06dc2?key_id=rzp_test_i00i1DaqSdP1bj&quot; method=&quot;post&quot;>\n    &lt;input id=&#39;otp&#39; type=&quot;hidden&quot; name=&quot;otp&quot; maxlength=&quot;6&quot;>\n  &lt;/form>\n  &lt;form id=&quot;form2&quot; name=&quot;form2&quot;>\n    &lt;input type=&quot;hidden&quot; name=&quot;type&quot; value=&quot;otp&quot;>\n    &lt;input type=&quot;hidden&quot; name=&quot;gateway&quot; value=&quot;eyJpdiI6ImUrXC8zWktKRFFycUdnS04zU3pybTV3PT0iLCJ2YWx1ZSI6ImM1dlNmR2pGQ3czZlM2cnZVNEQ3bnh0NlFkUmY2STdpSmowXC9ETW9LV0dZPSIsIm1hYyI6IjlkNTVhNjU5Y2NiMzA5MTdhMTNmYjU0YmI4MjgwOGQ2NzY3OTFlYTVlOGNiZDA4NGIwMDU1NGEzZjAxMzgxZjUifQ==&quot;>\n  &lt;/form>\n&lt;/body>\n&lt;/html>\n",
    "payment_id": 1013174,
    "order_id": 33902,
    "amount_in_paise": 500,
    "response_code": 1,
    "response_message": "Payment Successful!"
}
```
```json 400 Bad Request
{}
```

**Response Parameters** 

| Parameter Name   | Type   | Description                           |
| :--------------- | :----- | :------------------------------------ |
| content          | string | Html content to load the output data. |
| payment_id       | long   | Unique payment id.                    |
| order_id         | long   | Unique order id.                      |
| amount_in_paise  | long   | Amount paid in paise.                 |
| response_code    | string | Response code.                        |
| response_message | string | Short message about code.             |
