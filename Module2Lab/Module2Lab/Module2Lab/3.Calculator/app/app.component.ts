import { Component } from '@angular/core';
import {FormControl} from '@angular/forms';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'form2';
  a=new FormControl('')
  b=new FormControl('')
  result=null;
Add(){
  this.result=parseInt(this.a.value)+parseInt(this.b.value);
  }
  Subtract(){
    this.result=parseInt(this.a.value)-(parseInt(this.b.value));
    }
    Multiply(){
      this.result=parseInt(this.a.value)*parseInt(this.b.value);
      }
      Divide(){
        this.result=parseInt(this.a.value)/parseInt(this.b.value);
        }

}

