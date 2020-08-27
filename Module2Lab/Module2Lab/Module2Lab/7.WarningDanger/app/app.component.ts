import { Component } from '@angular/core';
import {FormControl} from '@angular/forms';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  notify:boolean=true;

  classes={}
  change(){
  if(!this.notify){
this.classes={
  danger:true,
  warning:false
  
}
this.notify=!this.notify;
  }
  else{
    this.classes={
      danger:false,
      warning:true
      
    }
    this.notify=!this.notify;
  }
}
}

