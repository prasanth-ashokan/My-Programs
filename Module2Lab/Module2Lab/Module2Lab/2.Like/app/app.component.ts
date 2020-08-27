import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'form2';
  count=99;
clicked(){
  if(this.count==99){
    this.count=100;
  }
  else{
    this.count=99;
  }
}
}
