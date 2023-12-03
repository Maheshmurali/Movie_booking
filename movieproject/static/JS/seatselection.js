let numberOfSeat=0;
for (let index = 0; index < document.querySelectorAll(".chair").length; index++) {
    document.querySelectorAll("li")[index].addEventListener("click",function () {
        var chairList = this.classList;
        var id = this.id;
        if(chairList.contains("chairselect")){
            chairList.remove("chairselect");
            numberOfSeat = numberOfSeat-1;
        }else{
            chairList.add("chairselect");
            numberOfSeat = numberOfSeat+1;
        }
        document.querySelector("#amount").innerHTML="BookNow"+"("+numberOfSeat*250+")";
    });
    
}
