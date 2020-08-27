import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {FormsModule} from "@angular/forms";
import { FavouriteProgramFormComponent } from './favourite-program-form/favourite-program-form.component';

@NgModule({
  declarations: [
    AppComponent,
    FavouriteProgramFormComponent,

  ],
  imports: [
    BrowserModule,FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
 }
 
