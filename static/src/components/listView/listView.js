/* @odoo-module */

import {Component } from "@odoo/owl" ;
import {Registry } from "@web/core/registry";

export class listViewAction extends Component {
    static template = "owl_custom.ListView";

}
Registry.category("actions").add("owl_custom.action_list_view",listViewAction);
