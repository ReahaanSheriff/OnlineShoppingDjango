var ct=document.querySelector("#ct");
var rm=document.querySelector("#rm");
var ad=document.querySelector("#ad");
var count=0;
ad.addEventListener("click",function(){
  count++;
  ct.textContent=count;
});

rm.addEventListener("click",function(){
  if (count != 0){
    count--;
   }
  ct.textContent=count;            
});