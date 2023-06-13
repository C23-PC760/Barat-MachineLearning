# Barat-MachineLearning
Sign Language Recognition : BARAT ( bahasa isyarat )
## System requirement
- python v3.9.2 
- tensorflow v2.10.1
- flask
- numpy
- python-dotenv

## System config
- edit `.env` file for and customize API_KEY (X-Auth-Token)

## Rest-api
The REST API to the example app is described below. <br>
Example request: `http://iniendpoint.com:5000/predict`

### Request
`Method: POST /predict` <br>
```javascript
header { 
    X-Auth-Token: '123456' // string
}
```
<br>
`type : multipart/form-data`
```javascript
body { 
    file : ini_file.jpg // file
}
```
<br>
### Response
```javascript
body { 
    error: False, // boolean
    message: 'Success', // string
    result: 'Hasil prediksi' // string
}
```
