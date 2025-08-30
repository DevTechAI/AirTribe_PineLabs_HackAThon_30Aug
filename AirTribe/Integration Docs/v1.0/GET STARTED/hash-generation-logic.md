---
title: "Hash Generation Logic"
slug: "hash-generation-logic"
excerpt: "Use this logic to generate an SHA256 hash of base64 encoded request."
hidden: false
createdAt: "Wed Oct 13 2021 08:20:14 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Sat Apr 20 2024 17:30:30 GMT+0000 (Coordinated Universal Time)"
---
```csharp
public static string GetSHAGenerated(string request, string secureSecret)
{
string hexHash = String.Empty;

byte[] convertedHash = new byte[secureSecret.Length / 2];
for (int i = 0; i < secureSecret.Length / 2; i++)
	{
convertedHash[i] = (byte)int.Parse(secureSecret.Substring(i * 2, 2), System.Globalization.NumberStyles.HexNumber);
	}


using (HMACSHA256 hasher = new HMACSHA256(convertedHash))
	{
byte[] hashValue = hasher.ComputeHash(Encoding.UTF8.GetBytes(request));
foreach (byte b in hashValue)
		{
hexHash += b.ToString("X2");
		}
	}

return hexHash;
}
```
```python
import hmac  
import hashlib  
import binascii

def signature(key, msg):  
    key = binascii.unhexlify(key)  
    msg = msg.encode()  
    return hmac.new(key, msg, hashlib.sha256).hexdigest().upper()
```
```java NodeJS
import jsSHA from "jssha";
static ValidateSecureIncomingRequest = (
    request: string,
    secureSeret: string
  ): boolean => {
    let shaGenerated: string = "";
    let shaObj = new jsSHA("SHA-256", "TEXT");
    shaObj.setHMACKey(secureSeret, "HEX");
    shaObj.update(request);
    shaGenerated = shaObj.getHMAC("HEX");
   
  };
```
```java
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class hash {
    public static String GenerateHash(String input, String strSecretKey) {
        String strHash = "";
        try {
            if (!isValidString(input) || !isValidString(strSecretKey)) {
                return strHash;
            }
            byte[] convertedHashKey = new byte[strSecretKey.length() / 2];

            for (int i = 0; i < strSecretKey.length() / 2; i++) {
                convertedHashKey[i] =
                        (byte)Integer.parseInt(strSecretKey.substring(i * 2, (i*2)+2),16); //hexNumber radix
            }
            strHash = hmacDigest(input.toString(), convertedHashKey,
                    "HmacSHA256");
        } catch (Exception ex) {
            strHash = "";
        }
        return strHash.toUpperCase();
    }
    private static String hmacDigest(String msg, byte[] keyString, String algo) {
        String digest = null;
        try {
            SecretKeySpec key = new SecretKeySpec(keyString, algo);
            Mac mac = Mac.getInstance(algo);
            mac.init(key);
            byte[] bytes = mac.doFinal(msg.getBytes("UTF-8"));
            StringBuffer hash = new StringBuffer();
            for (int i = 0; i < bytes.length; i++) {
                String hex = Integer.toHexString(0xFF & bytes[i]);
                if (hex.length() == 1) {
                    hash.append('0');
                }
                hash.append(hex);
            }
            digest = hash.toString();
        } catch (UnsupportedEncodingException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        } catch (InvalidKeyException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        } catch (NoSuchAlgorithmException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        }
        return digest;
    }
    public static boolean isValidString(String str){
        if(str != null && !"".equals(str.trim())){
            return true;
        }
        return false;
    }
}
```
```php
<?php

        global $hash;

 

        $secret_key = "688F0572F89242999F570D42C527Axxx";    


        function Hex2String($hex)

        {

            $string='';


            for ($i=0; $i < strlen($hex)-1; $i+=2)

            {

                $string .= chr(hexdec($hex[$i].$hex[$i+1]));

            }


            return $string;

        }


        $secret_key=Hex2String($secret_key);

        $strFormdata = 'eyJtZXJjaGFudF9kYXRhIjp7Im1lcmNoYW50X2lkIjoiMTE4NTAiLCJtZXJjaGFudF9hY2Nlc3NfY29kZSI6IjE0ODFlYTgwLTA2ZjAtNDMxNC04MzQ3LTVhYjFiZWE4ZmRjYiIsIm1lcmNoYW50X3JldHVybl91cmwiOiJodHRwczovL3h5eiIsIm1lcmNoYW50X29yZGVyX2lkIjoiMjFfMDZfMjAyMl8xN18zMl8zMiJ9LCJwYXltZW50X2luZm9fZGF0YSI6eyJhbW91bnQiOjEwMDAwLCJjdXJyZW5jeV9jb2RlIjoiSU5SIiwib3JkZXJfZGVzYyI6IlRlc3QgT3JkZXIifSwiY3VzdG9tZXJfZGF0YSI6eyJjb3VudHJ5X2NvZGUiOiI5MSIsIm1vYmlsZV9udW1iZXIiOiI5OTk5OTk5OTk5IiwiZW1haWxfaWQiOiJ0ZXN0QHBpbmVsYWJzLmNvbSJ9LCJiaWxsaW5nX2FkZHJlc3NfZGF0YSI6eyJmaXJzdF9uYW1lIjoiQWtoaWwiLCJsYXN0X25hbWUiOiJCaGF0aWEiLCJhZGRyZXNzMSI6IkRlbGhpIiwiYWRkcmVzczIiOiJEZWxoaSIsImFkZHJlc3MzIjoiRGVsaGkiLCJwaW5fY29kZSI6IjExNTAwNSIsImNpdHkiOiJEZWxoaSIsInN0YXRlIjoiRGVsaGkiLCJjb3VudHJ5IjoiSW5kaWEifSwic2hpcHBpbmdfYWRkcmVzc19kYXRhIjp7ImZpcnN0X25hbWUiOiJBa2hpbCIsImxhc3RfbmFtZSI6IkJoYXRpYSIsImFkZHJlc3MxIjoiRGVsaGkiLCJhZGRyZXNzMiI6IkRlbGhpIiwiYWRkcmVzczMiOiJEZWxoaSIsInBpbl9jb2RlIjoiMTE1MDA1IiwiY2l0eSI6IkRlbGhpIiwic3RhdGUiOiJEZWxoaSIsImNvdW50cnkiOiJJbmRpYSJ9LCJwcm9kdWN0X2luZm9fZGF0YSI6eyJwcm9kdWN0X2RldGFpbHMiOlt7InByb2R1Y3RfY29kZSI6InRlc3Rwcm9kdWN0MDIiLCJwcm9kdWN0X2Ftb3VudCI6MTAwMDB9XX0sImFkZGl0aW9uYWxfaW5mb19kYXRhIjp7InJmdTEiOiJBREwtVGVzdCIsInJmdTIiOiJUZXN0X1VBVF9BREwiLCJyZnUzIjoiVGVzdGluZyNVQVQiLCJyZnU0IjoiVGVzdGluZ19VQVRfQURMIiwicmZ1NSI6IlRlc3RpbmcifX0';

        $hash = strtoupper(hash_hmac('sha256', $strFormdata, $secret_key));

        echo $hash

?>
```
