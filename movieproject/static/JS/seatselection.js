let numberOfSeat=0;
let id=[];  
for (let index = 0; index < document.querySelectorAll(".chair").length; index++) {
    document.querySelectorAll("li")[index].addEventListener("click",function () {
        var chairList = this.classList;
        if(chairList.contains("chairselect")){
            chairList.remove("chairselect");
            numberOfSeat = numberOfSeat-1;
            id.pop(this.id);
        }else{
            chairList.add("chairselect");
            numberOfSeat = numberOfSeat+1;
            id.push(this.id);
        }
        document.querySelector("#amount").innerHTML="Book Now"+"("+numberOfSeat*250+")";
        document.querySelector("#noOfSeat").innerHTML=numberOfSeat;
        document.querySelector("#seat").innerHTML=id;
        document.querySelector("#price").innerHTML=numberOfSeat*250;

        var sNumber =  document.querySelector("#snumber");
        var seatNumber =  document.querySelector("#seatNumber");
        var amount =  document.querySelector("#tamount");
        sNumber.value = numberOfSeat;
        seatNumber.value = id;
        amount.value = numberOfSeat*250;
       
        var day = document.querySelector("#showday");
        var time = document.querySelector("#showtime");
        day.value = document.querySelector("#getDay").value;
        time.value = document.querySelector("#getShow").value;
    });
 
   
}


       





