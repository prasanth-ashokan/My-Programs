import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.css']
})
export class ShopComponent implements OnInit {
shop={
  'chocolate':'100',
  'parleg':'10',
  'eclairs':'2',
  'soap':'10'
}

  constructor() { }

  ngOnInit() {
  }
}
