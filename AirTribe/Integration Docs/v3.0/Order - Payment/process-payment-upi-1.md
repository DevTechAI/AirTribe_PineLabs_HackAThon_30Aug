---
title: "Process Payment UPI"
slug: "process-payment-upi-1"
excerpt: "Use the below endpoint to Process Payment UPI."
hidden: true
createdAt: "Fri Feb 04 2022 06:41:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:50:25 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "vpa\\*",
    "0-1": "string",
    "0-2": "VPA or UPI ID of the customer. For example, 9722xxx334@ybl.",
    "1-0": "is_upi_to_be_saved",
    "1-1": "string",
    "1-2": "If VPA or UPI ID is to be saved for the future transactions without providing VPA details again then the value in the filed is to be passed is \"true\". Else the value passed it \"false\".",
    "2-0": "country_code",
    "2-1": "string  \n(Length = 10 Characters)",
    "2-2": "The country code of the mobile number of the customer. Country code for India is 91.",
    "3-0": "mobile_number",
    "3-1": "string  \n(Length = 20 Characters)",
    "3-2": "Mobile number of the customer.",
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
    "upi_data": {
        "vpa": "test5@upi",
        "is_upi_to_be_saved": true,
        "upi_option": "UPI"
    },
    "customer_data": {
        "country_code": "91",
        "mobile_no": "9582492891",
        "email_id": "test_customer@abc.com"
    }
}
```

**Response Payload:** 

```json 200 Success
{
"content": "&lt;!DOCTYPE html&gt;\n&lt;html&gt;\n&lt;head&gt;\n &lt;title&gt;Payment in progress • Razorpay&lt;/title&gt;\n &lt;meta http-equiv=&quot;X-UA-Compatible&quot; content=&quot;IE=edge&quot;&gt;\n &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;\n &lt;style&gt;\n @-webkit-keyframes spin {\n 0%{-webkit-transform:scale(0.5);opacity:0;border-width:8px}\n 20%{-webkit-transform:scale(0.6);opacity:0.8;border-width:4px}\n 90%{-webkit-transform: scale(1);opacity:0}\n }\n @-moz-keyframes spin {\n 0%{-moz-transform:scale(0.5);opacity:0;border-width:8px}\n 20%{-moz-transform:scale(0.6);opacity:0.8;border-width:4px}\n 90%{-moz-transform:scale(1);opacity:0}\n }\n @keyframes spin {\n 0% {transform:scale(0.5);opacity:0;border-width:8px}\n 20% {transform:scale(0.6);opacity:0.8;border-width:4px}\n 90% {transform:scale(1);opacity:0}\n }\n\n html,body {\n font-family:&#39;lato&#39;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Roboto&quot;, &quot;Oxygen&quot;, &quot;Ubuntu&quot;, &quot;Cantarell&quot;, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;\n background: #FBFBFB;\n text-align: center;\n }\n\n .spin {\n width: 60px;\n height: 60px;\n margin: 0 auto;\n }\n\n .spin div {\n width: 100%;\n height: 100%;\n vertical-align: middle;\n display: inline-block;\n border-radius: 50%;\n border: 4px solid #3395ff;\n -webkit-animation: spin 1.3s linear infinite;\n -moz-animation: spin 1.3s linear infinite;\n -ms-animation: spin 1.3s linear infinite;\n -o-animation: spin 1.3s linear infinite;\n animation: spin 1.3s linear infinite;\n box-sizing: border-box;\n opacity: 0;\n }\n\n .spin2 {\n margin: -60px auto 0;\n }\n\n .spin2 div {\n animation-delay: 0.65s;\n }\n\n #spinner {\n margin: 20px 0 60px;\n }\n\n #content {\n max-width: 400px;\n margin: 0 auto;\n padding: 10px;\n box-sizing: border-box;\n position: relative;\n }\n\n .card {\n background: white;\n border-radius: 2px;\n box-shadow: 0px 4px 20px rgba(0,0,0,0.10);\n padding-bottom: 1px;\n }\n\n #message-txt b {\n display: block;\n font-size: 20px;\n padding: 0 25px 25px;\n }\n\n #message-txt {\n line-height: 26px;\n padding: 50px 30px 30px;\n font-size: 16px;\n opacity: 0.8;\n }\n\n .banner {\n padding: 24px;\n }\n\n .buttons {\n margin-top: 18px;\n line-height: 56px;\n }\n\n #retry-btn {\n background: #3395ff;\n color: #fff;\n cursor: pointer;\n }\n\n #cancel-btn {\n color: #3395ff;\n border-top: 1px solid #ececec;\n cursor: pointer;\n }\n\n .hide {\n display: none !important;\n }\n\n form {\n visibility: hidden;\n }\n\n &lt;/style&gt;\n&lt;/head&gt;\n&lt;body&gt;\n &lt;div id=&#39;content&#39;&gt;\n &lt;div class=&quot;banner&quot;&gt;\n \n &lt;/div&gt;\n\n &lt;div class=&quot;card&quot;&gt;\n &lt;div id=&#39;message-txt&#39;&gt;\n Please accept the collect request sent to your UPI app\n &lt;/div&gt;\n\n &lt;div id=&quot;spinner&quot;&gt;\n &lt;div class=&quot;spin&quot;&gt;&lt;div&gt;&lt;/div&gt;&lt;/div&gt;\n &lt;div class=&quot;spin spin2&quot;&gt;&lt;div&gt;&lt;/div&gt;&lt;/div&gt;\n &lt;/div&gt;\n\n &lt;div class=&quot;buttons&quot;&gt;\n &lt;div id=&quot;cancel-btn&quot;&gt;&lt;b&gt;Cancel Payment&lt;/b&gt;&lt;/div&gt;\n &lt;div class=&quot;hide&quot; id=&quot;retry-btn&quot; onclick=&quot;initUpiActivity()&quot;&gt;&lt;b&gt;Retry Payment&lt;/b&gt;&lt;/div&gt;\n &lt;/div&gt;\n &lt;/div&gt;\n\n &lt;div class=&quot;banner&quot;&gt;\n &lt;img src=&quot;https://cdn.razorpay.com/logo.png" id=&quot;logo&quot; height=&quot;28px&quot; style=&quot;height: 28px; margin: 20px auto;display: block;&quot;&gt;\n &lt;/div&gt;\n \n &lt;form id=&quot;form&quot; method=&quot;post&quot;&gt;&lt;/form&gt;\n &lt;form id=&quot;form2&quot; name=&quot;form2&quot;&gt;\n &lt;input name=&quot;type&quot; id=&quot;form2_type&quot; value=&quot;async&quot;&gt;\n &lt;input name=&quot;gateway&quot; id=&quot;form2_gateway&quot; value=&quot;eyJpdiI6IndDUTZcL1wveFM2bnAraDZnM09rMHFmdz09IiwidmFsdWUiOiJUc1hWeTEwVEgzcmtUUVM5VWJMYyt5TzJvRjVwKzkyNTFmUGJlZEdNSjl3PSIsIm1hYyI6IjM3MTU0NjAzYjQ0MjFkMmY4YTBiNzNlM2RiY2U0MTkxYjg2MjVlNDFjOWY1NWE5NTRhMmY1MmYzZGY0N2M1NTQifQ==&quot;&gt;\n &lt;/form&gt;\n &lt;/div&gt;\n\n &lt;script type=&quot;text/javascript&quot;&gt;\n // Async Payment data //\n var data = {&quot;type&quot;:&quot;async&quot;,&quot;method&quot;:&quot;upi&quot;,&quot;provider&quot;:null,&quot;version&quot;:1,&quot;payment_id&quot;:&quot;pay_I7HPYZHDf6Ctgi&quot;,&quot;gateway&quot;:&quot;eyJpdiI6IndDUTZcL1wveFM2bnAraDZnM09rMHFmdz09IiwidmFsdWUiOiJUc1hWeTEwVEgzcmtUUVM5VWJMYyt5TzJvRjVwKzkyNTFmUGJlZEdNSjl3PSIsIm1hYyI6IjM3MTU0NjAzYjQ0MjFkMmY4YTBiNzNlM2RiY2U0MTkxYjg2MjVlNDFjOWY1NWE5NTRhMmY1MmYzZGY0N2M1NTQifQ==&quot;,&quot;data&quot;:null,&quot;request&quot;:{&quot;url&quot;:&quot;https:\\/\\/api.razorpay.com\\/v1\\/payments\\/pay_I7HPYZHDf6Ctgi\\/status?key_id=rzp_test_i00i1DaqSdP1bj&quot;,&quot;method&quot;:&quot;get&quot;},&quot;org_logo&quot;:&quot;&quot;,&quot;org_name&quot;:&quot;Razorpay Software Private Ltd&quot;,&quot;checkout_logo&quot;:&quot;https:\\/\\/cdn.razorpay.com\\/logo.png&quot;,&quot;custom_branding&quot;:false,&quot;language_code&quot;:&quot;en&quot;,&quot;nobranding&quot;:false};\n // Async Payment data //\n\n try { CheckoutBridge.setPaymentID(data.payment_id) } catch(e){}\n\n var request_url = data.request.url;\n var key_id = &#39;rzp_test_i00i1DaqSdP1bj&#39;;\n var payment_base = &#39;https://api.razorpay.com/v1/payments/' + data.payment_id;\n var cancel_url = payment_base + &#39;/cancel?key_id=&#39;+key_id;\n var callback_url = payment_base + &#39;/redirect_callback?key_id=&#39;+key_id;\n\n var $ = function (id) {\n return document.getElementById(id);\n }\n\n if (!Date.now) {\n Date.now = function () { return +new Date(); };\n }\n\n var form = $(&#39;form&#39;);\n var CheckoutBridge = window.CheckoutBridge;\n var iosBridge = window.webkit &amp;&amp; webkit.messageHandlers &amp;&amp; webkit.messageHandlers.CheckoutBridge;\n var isIntentFlow = (CheckoutBridge || iosBridge) &amp;&amp; data.type === &#39;intent&#39;;\n\n if (data.type === &#39;async&#39; &amp;&amp; data.method === &#39;app&#39; &amp;&amp; data.provider === &#39;cred&#39;) {\n $(&#39;message-txt&#39;).innerText = &#39;Please complete the payment on the CRED app&#39;;\n }\n\n var lastXhr, lastPollTS, lastPollUrl;\n var threshold = 1000 * 20;\n var pollRetriesOnError = 5;\n var pollRetriesSoFar = 0;\n\n onfocus = function(e) {\n if (lastPollTS) {\n \n var timeSince = Date.now() - lastPollTS;\n\n \n if (lastPollUrl === request_url &amp;&amp; timeSince &gt; threshold) {\n lastXhr.abort();\n fetch(request_url, 1);\n track(&#39;ajax_periodic_retry&#39;, {\n last: {\n status: lastXhr.status,\n url: lastXhr.url,\n text: lastXhr.responseText\n },\n focus: !!e,\n time: timeSince\n })\n }\n }\n }\n\n \n setInterval(onfocus, 1000);\n\n \n\n function track(name, properties, cb) {\n setTimeout(function() {\n properties.CheckoutBridge = !!CheckoutBridge;\n properties.pageData = {\n type: data.type,\n data: data.data,\n key: key_id,\n payment_id: data.payment_id\n }\n var payload = {\n context: {\n user_agent: null\n },\n events: [{\n event: name,\n properties: properties,\n timestamp: Date.now()\n }]\n };\n\n if (key_id.slice(0, 5) === &#39;rzp_t&#39;) return console.log(payload);\n var call = new XMLHttpRequest();\n call.open(&#39;post&#39;, &#39;https://lumberjack.razorpay.com/v1/track', true);\n call.setRequestHeader(&#39;Content-Type&#39;, &#39;application/x-www-form-urlencoded&#39;);\n\n \n if (cb) {\n call.onreadystatechange = function() { if (call.readyState === 2) { cb() } }\n setTimeout(cb, 4e3);\n }\n\n call.send(&#39;key=MC40OTMwNzgyMDM3MDgwNjI3Nw9YnGzW&amp;data=&#39; +\n encodeURIComponent(btoa(JSON.stringify(payload))));\n })\n }\n\n function paymentCallback(data) {\n if (window.CheckoutBridge) {\n CheckoutBridge.oncomplete(JSON.stringify(data));\n } else if (iosBridge) {\n iosBridge.postMessage({\n action: &#39;success&#39;,\n body: data\n });\n } else {\n try { window.opener.onComplete(data) } catch(e){}\n try { (window.opener || window.parent).postMessage(data, &#39;*&#39;) } catch(e){}\n setTimeout(close, 999);\n }\n }\n\n function openIntentUrl(intentUrl, payment_id) {\n if (window.CheckoutBridge) {\n CheckoutBridge.callNativeIntent(intentUrl);\n } else if (iosBridge) {\n iosBridge.postMessage({\n action: &#39;callNativeIntent&#39;,\n body: {\n intent_url: intentUrl,\n payment_id: payment_id\n }\n });\n }\n }\n\n \n\n var submitted_count = 0;\n function submitForm(response) {\n \n setTimeout(function() {\n track(&#39;no_redirect&#39;, {\n count: ++submitted_count\n });\n if (submitted_count &amp;&amp; !(submitted_count % 2) &amp;&amp; submitted_count &lt; 10) {\n submitForm(response);\n }\n }, 10000);\n if (isIntentFlow) {\n paymentCallback(response);\n } else {\n if (response &amp;&amp; response.type === &#39;return&#39;) {\n var req = response.request;\n var content = req.content;\n form.action = req.url;\n form.method = req.method;\n form.innerHTML = Object.keys(content)\n .map(function (name) { return &#39;&lt;input name=&quot;&#39; + name + &#39;&quot; value=&quot;&#39; + content[name] + &#39;&quot;&gt;&#39; })\n .join(&#39;&#39;)\n } else {\n form.action = callback_url;\n }\n form.submit();\n }\n }\n\n function fetch(url, immediate) {\n var totalCalls = 0;\n\n function fetchAgain(timeout) {\n totalCalls++;\n \n if (totalCalls &gt; 50 &amp;&amp; !(totalCalls % 10)) {\n track(&#39;call_count&#39;, {\n count: totalCalls,\n url: url\n });\n }\n\n if (totalCalls &gt; 180) {\n return submitForm();\n }\n\n setTimeout(function() {\n // If polling, set timestamp.\n lastPollUrl = url;\n lastPollTS = Date.now();\n\n lastXhr = new XMLHttpRequest();\n lastXhr.open(&#39;get&#39;, url, true);\n\n lastXhr.onreadystatechange = function() {\n if (lastXhr.readyState === 4 &amp;&amp; lastXhr.status) {\n var json;\n try {\n json = JSON.parse(lastXhr.responseText);\n if (!json || typeof json !== &#39;object&#39;) {\n throw &#39;non object:&#39; + json;\n }\n } catch(e) {\n json = {\n message: e.message,\n error: {\n description: &#39;Parsing error&#39;\n },\n xhr: {\n status: lastXhr.status,\n text: lastXhr.responseText,\n url: url\n }\n };\n }\n if (json.status === &#39;created&#39;) {\n return fetchAgain();\n } else {\n try {\n if (\n json.razorpay_payment_id ||\n json.error ||\n json.version === 1\n ) {\n return submitForm(json);\n }\n } catch(e) {\n return handleAjaxError(e);\n }\n }\n handleAjaxError();\n }\n }\n lastXhr.onerror = handleAjaxError;\n lastXhr.send(null);\n }, timeout || 4000);\n }\n\n fetchAgain(immediate);\n }\n\n if (isIntentFlow) {\n var intent_url = data.data.intent_url;\n var payment_id = data.payment_id;\n\n function initUpiActivity() {\n try {\n openIntentUrl(intent_url, payment_id);\n $(&#39;spinner&#39;).className = &#39;hide&#39;;\n $(&#39;retry-btn&#39;).className = &#39;hide&#39;;\n $(&#39;message-txt&#39;).innerHTML = iosBridge ? &quot;Please accept the request from Razorpay&#39;s VPA on your UPI app&quot; : &#39;&lt;b&gt;Select UPI App&lt;/b&gt;Payment will be made to Razorpay\\&#39;s VPA&#39;;\n window.pollStatus = function(resp) {\n if (!Object.keys(resp).length ||\n /txnId=(undefined|null|)(&amp;|$)/i.test(resp.response) ||\n \n (/txnId=YBL/i.test(resp.response) &amp;&amp; Object.keys(resp).indexOf(&#39;bleTxId&#39;) &lt; 0)\n ) {\n \n \n // if (resp.isWebviewVisible === false || key_id === &#39;rzp_live_5WqsyF9dNRzsmf&#39;) {\n fetchWait(cancel_url);\n // }\n // $(&#39;cancel-btn&#39;).className = &#39;&#39;;\n // $(&#39;retry-btn&#39;).className = &#39;&#39;;\n // $(&#39;message-txt&#39;).innerHTML = &#39;Payment did not complete&#39;;\n // $(&#39;spinner&#39;).className = &#39;hide&#39;;\n\n $(&#39;message-txt&#39;).innerHTML = &#39;Please wait..&#39;;\n $(&#39;spinner&#39;).className = &#39;&#39;;\n } else {\n fetchWait(request_url);\n }\n }\n } catch(e) {\n track(&#39;android_error&#39;, {\n error: e.message\n }, submitForm)\n }\n }\n initUpiActivity();\n } else {\n fetch(request_url);\n }\n\n $(&#39;cancel-btn&#39;).onclick = function() {\n fetchWait(cancel_url);\n }\n\n function fetchWait(url) {\n $(&#39;spinner&#39;).className = &#39;&#39;;\n $(&#39;cancel-btn&#39;).className = &#39;hide&#39;;\n $(&#39;retry-btn&#39;).className = &#39;hide&#39;;\n $(&#39;message-txt&#39;).innerHTML = &quot;Please wait...&quot;;\n fetch(url, 1);\n }\n\n function handleAjaxError(e) {\n var props = {\n text: lastXhr.responseText,\n status: lastXhr.status,\n url: lastPollUrl\n }\n if (e) {\n props.message = e.message;\n }\n\n \n track(&#39;ajax_error&#39;, props, !e &amp;&amp; submitForm);\n\n \n if (e &amp;&amp; pollRetriesSoFar &lt; pollRetriesOnError) {\n pollRetriesSoFar++;\n fetch(lastPollUrl);\n }\n }\n &lt;/script&gt;\n",
"payment_id": 433424,
"order_id": 106057,
"amount_in_paise": 1000000,
"merchant_name": null,
"merchant_logo": null,
"response_handler_url": "http://pluraldev.pinepg.in/api/v1/upi/razorpay/responsehandler",
"timer_page_time_out_in_seconds": 180,
"response_code": 1,
"response_message": "SUCCESS"
}
```
```json 400 Bad Request
{
    "response_code": 11001,
    "response_message": "Sorry, your transaction has failed."
}
```

**Response Parameters** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "content",
    "0-1": "string",
    "0-2": "Html content to load the output data.",
    "1-0": "payment_id",
    "1-1": "long",
    "1-2": "Unique payment id.",
    "2-0": "order_id",
    "2-1": "long",
    "2-2": "Unique order id.",
    "3-0": "amount_in_paise",
    "3-1": "long",
    "3-2": "Amount paid in paise.",
    "4-0": "merchant_name",
    "4-1": "string",
    "4-2": "Merchant name.",
    "5-0": "merchant_logo",
    "5-1": "string",
    "5-2": "Merchant logo.",
    "6-0": "response_handler_url",
    "6-1": "string",
    "6-2": "Response handler url.",
    "7-0": "timer_page_time  \n\\_out_in_seconds",
    "7-1": "string",
    "7-2": "Timer count.",
    "8-0": "response_code",
    "8-1": "string",
    "8-2": "Response code.",
    "9-0": "response_message",
    "9-1": "string",
    "9-2": "Short message about code."
  },
  "cols": 3,
  "rows": 10,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
