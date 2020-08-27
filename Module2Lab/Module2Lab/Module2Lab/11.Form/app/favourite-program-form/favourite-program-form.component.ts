import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-favourite-program-form',
  templateUrl: './favourite-program-form.component.html',
  styleUrls: ['./favourite-program-form.component.css']
})
export class FavouriteProgramFormComponent implements OnInit {
 
  programs=[    {"name":"C"},
  {"name":"C++"},
  {"name":"JAVA"},
  {"name":"PYTHON"},
  {"name":"JAVA"}];
count:number=0;
flag:boolean=true;
changed(this){
  this.count= 0;
  this.programs.forEach(item=>{
    if(item.checked){
      this.count= this.count+1
    }  
  } )
  if(this.count>1){
    this.flag=false;
  }
  else{
    this.flag=true;
  }
  
}
  constructor() {
  }
   

  ngOnInit() {
    
  }
  

}
