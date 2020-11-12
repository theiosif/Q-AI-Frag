import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import {Observable} from "rxjs";
import {map} from "rxjs/operators";

import {
  InParameters,
  BuildResult
} from "./types";

const SERVER_URL: string = 'api/';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {
  }

  public frag(inParameters: InParameters){
    console.log('>>>>>>>> calling service')
    return this.http.post('${SERVER_URL}frag', inParameters).pipe(map((result:BuildResult) =>result));
  }
}
