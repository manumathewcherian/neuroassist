const database = firebase.database();
const usersRef = database.ref('/EEG');

usersRef.on('value' , function (snapshot){
    var data =snapshot.val();
    document.getElementById("connection").innerHTML=data.connection;
    document.getElementById("serialno").innerHTML=data.serialno;
    document.getElementById("signallevel").innerHTML=data.signallevel;
    document.getElementById("raweeg").innerHTML=data.raweeg;
    document.getElementById("attention").innerHTML=data.attention;
    document.getElementById("meditation").innerHTML=data.meditation;
    document.getElementById("delta").innerHTML=data.delta;
    document.getElementById("theta").innerHTML=data.theta;
    document.getElementById("lowalpha").innerHTML=data.lowalpha;
    document.getElementById("highalpha").innerHTML=data.highalpha;
    document.getElementById("lowbeta").innerHTML=data.lowbeta;
    document.getElementById("highbeta").innerHTML=data.highbeta;
    document.getElementById("lowgamma").innerHTML=data.lowgamma;
    document.getElementById("highgamma").innerHTML=data.highgamma;
    document.getElementById("blinkstrength").innerHTML=data.blinkstrength;
    document.getElementById("executedaction").innerHTML=data.executedaction;
})