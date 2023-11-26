
  var clientID = "VaKxfD6BQ36xsiShgy8lQ";
  var clientSecret = "mWXjoGMBBiuqDUsqFj1VFbdLE0yCBhdS";




function onOpen(){
  let ui= SpreadsheetApp.getUi();
  ui.createMenu('Hold_Zoom')
    .addItem('getDate', 'Hold_Zoom')
    .addToUi();
}



function Hold_Zoom() {
  var sheet = SpreadsheetApp.getActiveSheet();


  var clientID = "VaKxfD6BQ36xsiShgy8lQ";
  var clientSecret = "mWXjoGMBBiuqDUsqFj1VFbdLE0yCBhdS";
  var encodedKeys = Utilities.base64Encode(clientID + ":" +clientSecret);



//  https://script.google.com/macros/s/AKfycbwOqtGBih8XmiyZeTiziKWWr6QVYFgw43l4q55cBhWlSCR3CLoOXXQtb0lyrBEB6TLnMg/exec

  var redirectURI = "https://script.google.com/macros/s/AKfycbwOqtGBih8XmiyZeTiziKWWr6QVYFgw43l4q55cBhWlSCR3CLoOXXQtb0lyrBEB6TLnMg/usercallback";

  // var response = UrlFetchApp.fetch("http://zoom.us/oauth/token?grant_type=authorization_code&code=" + authCodeClean + "&redirect_url=" + returnUrl, options);

  var scopes = "meeting:write:admin,meeting:master,meeting:read:admin,user:master,user:read:admin,user:write:admin";



  var authorizationUrl = "https://zoom.us/oauth/authorize?response_type=code&client_id=" + clientID + "&redirect_uri=" + redirectURI + "&scope=" + scopes;
  // var authDialog = HtmlService.createHtmlOutput("<script>window.google.com.location.href='" + authorizationUrl + "';</script>");
  // SpreadsheetApp.getUi().showModalDialog(authDialog, "Authorize this app");

  var authDialog = HtmlService.createHtmlOutput("<script>window.open('" + authorizationUrl + "', '_blank', 'height=500,width=600');google.script.host.close();</script>");
  SpreadsheetApp.getUi().showModalDialog(authDialog, "Authorize this app");



}

function doGet(e) {
  var sheet = SpreadsheetApp.openById("1I_YtIAGeUqwHnrKURYViHeq1NwaE-Ob31qXRafQeKMY");

  var authCode = e.parameter.code;


  sheet.getRange("G2").setValue(authCode);

  
  var tokenUrl = "https://zoom.us/oauth/token"; //+ authCode;
  var tokenOptions = {
    "method": "post",
    "contenType": "application/x-www-form-urlencoded",
    "headers": {
                "Authorization": "Basic " + Utilities.base64Encode(clientID + ":" +clientSecret),
                },
    "payload": {
             code: authCode,
             grant_type: "authorization_code",
             redirect_uri: "https://script.google.com/macros/s/AKfycbwOqtGBih8XmiyZeTiziKWWr6QVYFgw43l4q55cBhWlSCR3CLoOXXQtb0lyrBEB6TLnMg/usercallback"
             }
  };

  var tokenResponse = UrlFetchApp.fetch(tokenUrl, tokenOptions);
  var tokenData = JSON.parse(tokenResponse.getContentText());

  var accessToken = tokenData.access_token;

  sheet.getRange("H2").setValue(accessToken);
  
  
  

  getAuthorizeCode(authCode);
  return HtmlService.createHtmlOutput("Authorization successful. You can close this window and return to the spreadsheet.");

}

function debug(){
  getAuthorizeCode("MqmEYzNdAWxsHYRDqDWTG-8KXa5FAm9Qg")
}

function getAuthorizeCode(){


  var encodedKeys = Utilities.base64Encode(clientID + ":" +clientSecret);

  var redirectURI = "https://script.google.com/macros/s/AKfycbwOqtGBih8XmiyZeTiziKWWr6QVYFgw43l4q55cBhWlSCR3CLoOXXQtb0lyrBEB6TLnMg/usercallback";
  var scopes = "meeting:write:admin,meeting:master,meeting:read:admin,user:master,user:read:admin,user:write:admin";


  var sheet = SpreadsheetApp.openById("1I_YtIAGeUqwHnrKURYViHeq1NwaE-Ob31qXRafQeKMY");
  var date = sheet.getRange("A2").getValue();
  var time = sheet.getRange("B2").getValue();
  var year = date.getFullYear();
  var month = date.getMonth() + 1;
  var day = date.getDate() + 1;
  var hr = time.getHours();
  var min = time.getMinutes();
  var second = time.getSeconds();
  var topic = sheet.getRange("E2").getValue();
  var dateString = new Date(year + "-" + month + "-" + day); //+ "T" + hr + ":" + min  + ":" + second);
  var formatDate = Utilities.formatDate(dateString, 'GMT', 'yyyy-MM-dd');
  var timeString = new Date(formatDate + " " + (hr + ":" + min + ":" + second) + "Z");
  var formatTime = Utilities.formatDate(timeString, 'GMT+8', 'HH:mm:ss.SSS');

  var start_time = new Date(formatDate + "T" + formatTime).toISOString();
  var object = sheet.getRange("C2").getValue();
  var object_email = sheet.getRange("D2").getValue();
  var accessToken = sheet.getRange("H2").getValue();

  var options = {
    'method': "post",
    'headers': {"Authorization": "Bearer " + accessToken},
    'contentType': "application/json",
    'payload': JSON.stringify({
      "topic": topic,
      "type": 2,
      "start_time": start_time,
      "duration": 60,
      "timezone": "Asia/Hong_Kong",
      "agenda": "Zoom meeting with " + object,

      "settings": {
        "join_before_host": true,
        "host_video": true,
        "participant_video": true,
        "invitees": [
        {
          "email": object_email,
          "name" : object
        }
        ]
      }
    })
  };
  
  
  
  
  var response = UrlFetchApp.fetch("https://api.zoom.us/v2/users/me/meetings", options);
  var data = JSON.parse(response.getContentText());
  var join_url = data.join_url;
    
  sheet.getRange("F2").setValue(join_url);

  
}


const ZOOM_API_KEY = 'VaKxfD6BQ36xsiShgy8lQ';
const ZOOM_API_SECRET = 'XHeBFMK1j0XD1HWuV4uXKmSpHjyUMi9d';
const ZOOM_EMAIL = 'support@fromdb.com';


// doPOST


// function doGET(){
  
//   let spreadsheet= SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/1I_YtIAGeUqwHnrKURYViHeq1NwaE-Ob31qXRafQeKMY/edit#gid=0");
//   let sheet = spreadsheet.getSheetByName(Sheet1);

//   let data=[];
//   let record={};

//   record['date'] = sheet.getRange("A2").getValue();
//   record['time'] = sheet.getRange("B2").getValue();
//   record['topic'] = sheet.getRange("E2").getValue();
//   record['start_time'] = new Date(date + " " + time);
//   record['object'] = sheet.getRange("C2").getValue();
//   record['object_email'] = sheet.getRange("D2").getValue();
//   response = {record : []}
//   data.push(record);

//   // var zoom = Zoom.createSdkClient({ "apiKey": VaKxfD6BQ36xsiShgy8lQ, "apiSecret": XHeBFMK1j0XD1HWuV4uXKmSpHjyUMi9d });
//   // var meeting = zoom.meeting;
//   // var options = {
//   //   "topic": topic,
//   //   "type": 2,
//   //   "startTime": TO_DATE(start_time),
//   //   "durationInMinutes": 60,
//   //   "timezone": "Asia/Hong_Kong"
//   // };


//   var dataExportFormat = JSON.stringify(data);
//   return ContentService.createTextOutput(dataExportFormat).setMimeType(ContentService.MimeType.JSON);

//   meeting.create(options).then(function(result) {
//     Logger.log(result);
//   }).catch(function(error) {
//     Logger.log(error);
//   });



//   // if(!SpreadsheetApp.getActiveSheet().getRange("A2:E2").isBlank){

//   // }
// }













