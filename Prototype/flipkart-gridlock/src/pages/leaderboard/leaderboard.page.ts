import { Component } from '@angular/core';

import { NavController, AlertController } from 'ionic-angular';


@Component({
  selector: 'page-leaderboard',
  templateUrl: 'leaderboard.page.html'
})
export class LeaderBoardPage {
  public IP_ADDRESS: string;
  constructor(public navCtrl: NavController, public alertController: AlertController) {

  }

  

}