import { Component } from '@angular/core';
import {FormControl} from '@angular/forms';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  student={
    'RollNo':'17P237',
    'Name':'Prasanth',
    'DOB':'29/12/1999',
    'Department':'CSE'
  }
}

