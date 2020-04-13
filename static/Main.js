let canvas = document.querySelector("canvas");
let c = canvas.getContext('2d');

let x = 0;
let y = 0;

let points = [];
let obsticles = [];
let heights =[];

function addHeight() {
    var txt;
    var height = prompt("Enter height to ceiling at this point[m]:", "5");
    if (height == null || height == "") {
      txt = "User cancelled the prompt.";
    } else {
      heights.push(height);
      addPoints();
    }
  }


function makeCanvas(x,y){
    canvas.width = window.innerWidth/2;
    canvas.height = window.innerWidth/2*(y/x);
}

function grid(x,y){
    width = canvas.width / x;
    height = canvas.height/ y;
    for(let i= 0; i<= x; i++){
        for(let j =0; j<= y; j++){
            c.beginPath();
            c.rect(width*i,height*j, width, height);
            c.stroke();
        }
    }
}

function addPoints(){
    myPoints= '[';
    for(i in points){
        myPoints += '('+  points[i][0].toString() +','+  points[i][1].toString() +')';
        if(points.length-1 != i){
            myPoints+=','
        }
    }
    myPoints += ']';

    myObsticles= '[';
    for(i in obsticles){
        myObsticles += '('+  obsticles[i][0].toString() +','+  obsticles[i][1].toString() +')';

        console.log([obsticles.length-1, i]);
        if(obsticles.length-1 != i){
            myObsticles+=','
        }
    }
    myObsticles += ']';

    document.getElementById('test').innerHTML = "<form method= 'POST'> Heights <input type= 'text' name = 'heights' value =" +heights+"> Points <input type= 'text' name = 'points' value =" +myPoints+"> Obsticles <input type= 'text' name = 'obsticles' value =" +myObsticles+"><input type = 'submit' name='Generate rail' value='Generate rail'></form>";
}

function gridUpdate(event){
    width = canvas.width / x;
    height = canvas.height/ y;
    for(let i= 0; i<= x; i++){
        for(let j =0; j<= y; j++){
            c.beginPath();
            c.fillStyle = 'black';
            c.rect(width*i,height*j, width, height);
            if(event.offsetX>=width*i && event.offsetX<width*(i+1)
            && event.offsetY>= height*j && event.offsetY < height*(j+1)){
                c.fill();
                points.push([i,j])
                addPoints();

            }
            else{
                 c.stroke();
            }
        }
    }
    addHeight();
}

function gridUpdateObsticle(event){
    console.log("obstic")
    width = canvas.width / x;
    height = canvas.height/ y;
    for(let i= 0; i<= x; i++){
        for(let j =0; j<= y; j++){
            c.beginPath();
            c.fillStyle = 'red';
            c.rect(width*i,height*j, width, height);
            if(event.offsetX>=width*i && event.offsetX< width*(i+1)
            && event.offsetY>= height*j && event.offsetY < height*(j+1)){
                c.fill();
                obsticles.push([i,j]);
                addPoints();
            }
            else{
                 c.stroke();
            }
        }
    }
}


function removeUpdate(event){
    width = canvas.width / x;
    height = canvas.height/ y;
    for(let i= 0; i<= x; i++){
        for(let j =0; j<= y; j++){
            c.beginPath();
            c.fillStyle = 'azure';
            c.rect(width*i,height*j, width, height);
            if(event.offsetX>=width*i && event.offsetX< width*(i+1)
            && event.offsetY>= height*j && event.offsetY < height*(j+1)){
                c.fill();

                for(var k = 0; k < points.length; k++) {
                    if(points[k][0] == i && points[k][1]){
                        console.log('yes');
                        points.splice(k, 1);
                        break;
                    }
                }

                for(var k = 0; k < obsticles.length; k++) {
                    if(obsticles[k][0] == i && obsticles[k][1]){
                        console.log('yes');
                        obsticles.splice(k, 1);
                        break;
                    }
                }

                addPoints();
            }
            else{
                 c.stroke();
            }
        }
    }
}


//setting gridSize:
let submit = document.getElementById('submit');
submit.addEventListener('click',function(){
    let myWidth = document.getElementById('width').value; // i meter
    let myHeight =document.getElementById('height').value;
    makeCanvas(myWidth,myHeight);
    x= myWidth*2; //500 mm i bredde og høyde
    y = myHeight*2;
    grid(x,y);
})



let point = document.getElementById('point');
let obstacle = document.getElementById('obstacle');
let remove = document.getElementById('remove');

function pointEvent(){
    canvas.removeEventListener('mousedown', gridUpdateObsticle);
    canvas.removeEventListener('mousedown', removeUpdate);
    canvas.addEventListener('mousedown',gridUpdate);
}

function obsticleEvent(){
    canvas.removeEventListener('mousedown', gridUpdate);
    canvas.removeEventListener('mousedown', removeUpdate);
    canvas.addEventListener('mousedown', gridUpdateObsticle);
}

function removeEvent(){
    canvas.removeEventListener('mousedown', gridUpdate);
    canvas.removeEventListener('mousedown', gridUpdateObsticle);
    canvas.addEventListener('mousedown', removeUpdate);
}
point.addEventListener('click',pointEvent);
obstacle.addEventListener('click', obsticleEvent);
remove.addEventListener('click', removeEvent);