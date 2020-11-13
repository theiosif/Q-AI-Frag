import { Component, OnInit } from '@angular/core';
import {ApiService} from "./api.service";

import {
  InParameters,
  OutResult
} from "./types";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Q-AI';

  //inputs need to be constructed
  public inParameters:InParameters = new InParameters();
  //outputs: we don't care about such stuff
  public outResult:OutResult; 


  constructor(private apiService: ApiService) {
  }

  ngOnInit() {
  }

  public frag() {
    this.apiService.frag(this.inParameters).subscribe((outResult) => {
        this.outResult = outResult;
    });
  }

  public wip(){
    alert("Coming soon.")
  }
}
