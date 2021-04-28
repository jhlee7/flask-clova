curl --location --request POST 'http://10.168.246.182:5000/user_defined' \
--header 'Content-Type:  application/json; charset=UTF-8' \
--data-raw '{
    "version": "0.1.0",
    "session": {},
    "context": {},
    "request": {
                "type": "IntentRequest",
                "intent": {
                    "domain": "HelloIntent",
                    "name": "HelloIntent.Reprompt",
                    "intentType": "Standard",
                    "slots": {}
                },
                "meta": {}
            }
}'


curl --location --request POST 'http://10.168.246.182:5000/user_defined' \
--header 'Content-Type:  application/json; charset=UTF-8' \
--data-raw '{
    "version": "0.1.0",
    "session": {},
    "context": {},
    "request": {
                "type": "IntentRequest",
                "intent": {
                    "domain": "HelloIntent",
                    "name": "HelloIntent.Hello",
                    "intentType": "Standard",
                    "slots": {}
                },
                "meta": {}
            }
}'

