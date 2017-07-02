import { Component } from '@angular/core';

import { NavController, AlertController } from 'ionic-angular';


@Component({
  selector: 'page-coupons',
  templateUrl: 'coupons.page.html'
})
export class CouponsPage {
  public IP_ADDRESS: string;
  constructor(public navCtrl: NavController, public alertController: AlertController) {

  }

  

}