---
title: "Process Card Payment via Saved Card Vault"
slug: "process-card-payment-via-saved-card-vault"
excerpt: "This API Help to Process Card Payment via Saved Card Vault."
hidden: true
metadata: 
  image: []
  robots: "index"
createdAt: "Fri Feb 04 2022 08:50:42 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Feb 09 2022 11:29:36 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Details",
    "0-0": "cvv\\*",
    "0-1": "string  \n(Length=6 Characters)",
    "0-2": "CVV of the card which has been saved and on which the payment is intended.",
    "1-0": "saved_card_token\\*",
    "1-1": "string",
    "1-2": "In the filed, the value of saved_credential_token received by the merchant in Fetch Vauld API.",
    "2-0": "mobile_number\\*",
    "2-1": "string  \n(Length = 20 Characters)",
    "2-2": "Mobile number of the customer.",
    "3-0": "country_code",
    "3-1": "string  \n(Length = 10 Characters)",
    "3-2": "The country code of the mobile number of the customer. Country code for India is 91.",
    "4-0": "email_id\\*",
    "4-1": "string  \n(Length = 100 Characters)",
    "4-2": "Email id of the cusotmer.",
    "5-0": "customer_token\\*",
    "5-1": "string",
    "5-2": "customer_token is the unique identifier of the customer. customer_token received in the response of Create Customer API is to be sent in this field."
  },
  "cols": 3,
  "rows": 6,
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
        "cvv": "***",
        "saved_card_token": "vQ7ssVqGlcfEUpGdzycwnQ=="
    },
    "customer_data": {
        "mobile_no": "90XXXXXX78",
        "country_code": "91",
        "email_id": "balwant.singh@pinelabs.com",
        "customer_token": "vQ7ssVqGlcfEUpGdzycwnQ=="
    }
}
```

**Response Payload:** 

```json 200 Success
{
    "content": "&lt;html>&lt;head>&lt;Meta HTTP-EQUIV=&quot;Cache-Control&quot; CONTENT=&quot;no-cache&quot; >&lt;Meta HTTP-EQUIV=&quot;Pragma&quot; CONTENT=&quot;no-cache&quot;>&lt;Meta HTTP-EQUIV=&quot;Expires&quot; CONTENT=&quot;0&quot;>&lt;title>Card Info&lt;/title>&lt;SCRIPT LANGUAGE = JavaScript>\n&lt;!--\nisNN = document.layers ? 1 : 0; \nfunction noContext(){return false;}\nfunction noClick(e){\nif(isNN){\nif(e.which > 1) {return false;}\n} else { \nif(event.button > 1){return false;}\n}\n}\nif(isNN){ \ndocument.captureEvents(Event.MOUSEDOWN);\n}\n\t\tdocument.oncontextmenu = noContext;\n\t\tdocument.onmousedown   = noClick;\n\t\tdocument.onmouseup     = noClick;\n //-->\n &lt;/SCRIPT>\n&lt;script language=&quot;javascript&quot;>window.history.forward(); function noBack() { window.history.forward(); } &lt;/script>&lt;style type=&quot;text/css&quot;> body { font-family: Arial, Helvetica, sans-serif; font-weight:normal; color:#474747; font-size: 14px; margin:15% auto 0 auto; } #intermediatepage { background-image:url(&#39;/images/ccavenue_logo.gif&#39;); background-position:center top; background-repeat:no-repeat; padding:10px 20px 0 20px;} #intermediatepage div.process { background-image:url(&#39;/images/loader.gif&#39;); background-position:center 35px; background-repeat:no-repeat;}&lt;/style> &lt;/head>&lt;body oncontextmenu=&quot;return false;&quot; onLoad=&quot;noBack();document.MalltoEpay.submit();&quot;>&lt;label id=&quot;requestId&quot; style=&quot;display:none;&quot;>110296807983&lt;/label>\n&lt;form name=&quot;MalltoEpay&quot; method=&quot;POST&quot; action=&quot;https://sbipg.sbi/PG/VPAS.htm&quot; >\n&lt;input type=&quot;hidden&quot; name=&quot;actionVPAS&quot; value=&quot;VbvVEReqProcessHTTP&quot;>\n&lt;input type=&quot;hidden&quot; name=&quot;trandata&quot; value=&quot;AC7B87F02E55C592B4DEBD10404A8B5AF495DA2B02E8655EB652C16DE13491A3148B23BB9E47C45F197445087A363866F25A7A809C60C354A81273D8E0E4B2D036AA600767D16AC94B7760E770C3BEF51B6420E4F4DA73F828FB6B616FB1F008B771262B2E349324C2C7C2BFFEC0459F0377FEA98985A95FC8DB2C4B97ACE84AD76DA38B5FC8638233581E5FC977CBD2BD0A485A0BDC5392C29C687C036124DB1F0520E8F2A84E35AE26A4197364008BF14B5A69B51E3C227FEB4713178527BB82B836265437CFDABF32F9D2D726018613EFD950F6EED3FBEC6FC388C08018A79161C66490F8E1B2E3ABB7039589810FC04512605EB9A0F8DD67DC8198FCC400F1EC32C908118652BE80DC38628FF5930CB847B3B0D541ECBF24F8C70B7D02E1ABDE11D194DDCD545C2DEE711DB1DD59B6CE5000D4363E89DCE14861A190351DEE91FE6C31D724E22B6FA0B03046EBF6B310628D27CDAA37BEE9BB731E71FF115BCBA14901255BD971800DCB0C4969D0B7B3980A00B9D1227BFD35CBB4A739A986FA4FC8772B6532B067DFA22A9A84BC6E5E4EBB7946158FC70A02EB599F6E0910DD58CE7AF965558AB2EAE8D1AC01CB631E94F4994092E1038A4C299064A25E2DB136D06E39BE5E3D58B5A4C10618A94CFE86DE95CED42FEC9751C1F5A0EA0DF99A117FFDC585FC1E1278883CEC206BC194F563DE8D1663B07C1A9C60B7D02912A3C11DFAD0707810B76C4D201692344739014F34DDE7BA0E4F9F30F576F7CF0410C9CF18BA0EE1EF3B27D222130D29D85198C6798CED12D116C0CBBEA0E0CE7934077A3662D45F8C477CFD32EB3B84DD67ECC29976B21BC1219C4AA6A91624F07DF50541E28457F4DDD531A25B12697A28933BA248EC77EE21C77E1699898E82DC8FF2A7D5CCFD5AEDD426D72FBC67840F50300230F8BB94EA704DC3626CB06D179A8E0746F9B816295F796E35C203ABB1F1E621183FF0AC8F35BF328FC3229065D098C98CC5B2A7B76D67FA9DBF100C52BC40B73B28AF74AA0148C32589B24CA7AFD7ECB559E7263980CE278EA16B2540AE4F5435FBF80D483E14BDD880048D248B568BA845009F93733F4FFEEEB88E7831D822B968AD0CA44C2EDF0754C7920EF555433AB73263F96A9A96FCB8511B763057B816C0AF96EFEA9E260A593818050EE71E41DF9F7D886284AA3B9D0DAF6E1B4D765B994F6EFFF93E83FFD0FE86C09E767B121C136BD54CF432AB3C5D36F0BF5AF8B3EBA4F3166C08E077C2609610C5FA503F52CF387C90493501D1ED4FEB239F74CFAFA7C5AC0DC6FD22949745ACCF7030A9C6EB395736C0EE2F8DB4D50E6C06C26E29086370DC826DEDF30F69D427E8F13BF77E2CE899C8751D5CC383FC3B189CAFF37EBD01DD86BFA95B9D51C23B8610CE49EE5F08F5C2C0D86EEA3CEB59C41BDBD81412DE713FF7F840CFE03BDE14FE57C16947A3E7865B17DED5E8A908A8D562DF3385438784355C96A0D1A62C4040676F5166B68228C6ACC44A2AD094DC6B7301171BB46AB5DC68E3114A09E117D5775966B2A6EF94FDCA082C983F9CCB1665F2C8B0311723893EDCE2DFA1802A2EA5F2CA44C73F1E29F475DDDC0FEC8BA23D35923CDB12A441788890&quot;>\n&lt;input type=&quot;hidden&quot; name=&quot;errorURL&quot; value=&quot;https://secure.ccavenue.com/receive/198/M_81800542/servlet/BankRespReceive&quot;>\n&lt;input type=&quot;hidden&quot; name=&quot;responseURL&quot; value=&quot;https://secure.ccavenue.com/receive/198/M_81800542/servlet/BankRespReceive&quot;>\n&lt;input type=&quot;hidden&quot; name=&quot;tranportalId&quot; value=&quot;81800543&quot;>\n&lt;/form>\n&lt;div id=&quot;intermediatepage&quot; align=&quot;center&quot;>&lt;div class=&quot;process&quot;>&lt;br />&lt;br />&lt;br />&lt;br />&lt;br />&lt;br />&lt;span class=&quot;content-text&quot; style=&quot;font-size:24px; font-weight:bold;&quot;>Please be patient while your transaction is being processed.&lt;/span>&lt;br style=&quot;line-height:35px;&quot; />&lt;span>Do not &quot;close the window&quot; or press &quot;refresh&quot; or &quot;browser back/forward button&quot;.&lt;/span>&lt;br />&lt;br />&lt;/div>&lt;/div>&lt;/body>&lt;/html>\n",
    "payment_id": 437532,
    "order_id": 106369,
    "amount_in_paise": 200,
    "response_code": 1,
    "response_message": "Payment Successful!"
}
```
```json 400 Bad Request
{}
```
