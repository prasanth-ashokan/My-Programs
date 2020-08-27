import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { UsernameValidators } from './username.validators';

@Component({
  selector: 'contact-form',
  templateUrl: './contact-form.component.html',
  styleUrls: ['./contact-form.component.css']
})
export class ContactFormComponent implements OnInit {

  userform = new FormGroup({
    username: new FormControl('',UsernameValidators.cannotContainSpaceSymbol),
    password: new FormControl('')
  })

  constructor() { }

  ngOnInit() {
  }

  get username() {
    return this.userform.get('username');
  }

  get password() {
    return this.userform.get('password');
  }

  fun() {
    console.log(this.userform);  
    console.log(this.userform.get('username'));
  }

}
