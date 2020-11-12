import { BrowserModule } from '@angular/platform-browser';
//import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {HttpClientModule} from "@angular/common/http";

import { FormsModule } from '@angular/forms';

import { ApiService } from './api.service';


//import {MatInputModule} from '@angular/material/input'
//import {MatCardModule} from '@angular/material/card';
//import {MatButtonModule} from '@angular/material/button';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    //BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    ///////////////
    //  MATERIAL //
    ///////////////,
    //MatInputModule,
    //MatCardModule,
    //MatButtonModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
