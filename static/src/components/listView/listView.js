/* @odoo-module */

import { Component } from "@odoo/owl" ;
import { registry } from "@web/core/registry";

export class listViewAction extends Component {
    static template = "owl_custom.ListView";

}
registry.category("actions").add("owl_custom.list_view_action", listViewAction) ;


