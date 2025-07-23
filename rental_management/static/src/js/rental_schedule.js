odoo.define('rental_management.RentalSchedule', function (require) {
    "use strict";

    const { Component } = owl;
    const { xml } = owl.tags;
    const { whenReady } = owl.utils;

    class RentalSchedule extends Component {
        static template = xml`
            <div class="rental_schedule">
                <h2>Rental Schedule</h2>
                <div class="schedule-container">
                    <!-- Schedule content will be rendered here -->
                </div>
            </div>
        `;

        setup() {
            super.setup();
            // Initialize schedule data
            this.state = {
                schedules: [],
            };
            this._loadData();
        }

        async _loadData() {
            const schedules = await this.env.services.rpc({
                model: 'rental.schedule',
                method: 'search_read',
                args: [[]],
                kwargs: {
                    fields: ['rental_product_id', 'rental_order_id', 'start_date', 'end_date', 'state'],
                },
            });
            this.state.schedules = schedules;
            this.render();
        }
    }

    function rentalScheduleApp() {
        const app = new Component(RentalSchedule);
        app.mount(document.querySelector('.rental_schedule_container'));
    }

    whenReady(rentalScheduleApp);

    return RentalSchedule;
});