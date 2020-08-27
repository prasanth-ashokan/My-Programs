import { Component } from '@angular/core';
import {FormGroup,FormControl} from '@angular/forms';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  userform=new FormGroup({
red:new FormControl(),
cyan:new FormControl(),
blue:new FormControl(),
green:new FormControl(),
yellow:new FormControl(),
violet:new FormControl()
  })
}
