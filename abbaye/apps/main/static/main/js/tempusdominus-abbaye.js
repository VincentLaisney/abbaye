const calendar = {
    localization: {
        dateFormats: {
            L: 'MM/dd/yyyy',
        },
        dayViewHeaderFormat: { month: 'long', year: 'numeric' },
        locale: 'fr-FR',
    },
    display: {
        components: {
            decades: true,
            year: true,
            month: true,
            date: true,
            hours: false,
            minutes: false,
            seconds: false
        },
        theme: 'light',
        viewMode: 'calendar',
    }
};

const clock = {
    localization: {
        dateFormats: {
            L: 'HH:mm',
        },
        locale: 'fr-FR',
    },
    display: {
        components: {
            decades: false,
            year: false,
            month: false,
            date: false,
            hours: true,
            minutes: true,
            seconds: false
        },
        theme: 'light',
        viewMode: 'clock',
    }
};