import moment from 'moment-timezone';
import 'moment/locale/fr-ca';
import { getLanguage } from './helper';

export const specificLocalizedMoment = (...args) => {
  let passedLocale;
  let passedTimeZone;

  if (
    args.length > 0 &&
    (Object.prototype.hasOwnProperty.call(args[args.length - 1], 'locale') ||
      Object.prototype.hasOwnProperty.call(args[args.length - 1], 'timeZone'))
  ) {
    const { locale, timeZone } = { ...args.pop() };
    passedLocale = locale;
    passedTimeZone = timeZone;
  }

  const instance = localizedMoment()(moment(...args));

  if (typeof passedLocale === 'string') {
    instance.locale(passedLocale);
  }
 if (typeof passedTimeZone === 'string') {
      if (moment.tz.zone(passedTimeZone)) {
        instance.tz(passedTimeZone);
      }
    }
  

  return instance;
};
@param {string} language
@return{moment}

const localizedMoment = (language = getLanguage()) => {
let momentLanguage=language;
  let momentLanguage = momentLanguage&&language.toLowerCase();

  switch (momentLanguage) {
    case 'en-us':
      momentLanguage = 'en';
      break;
    case 'en-ca':
      momentLanguage = 'en-ca';
      break;
    case 'fr-ca':
      momentLanguage = 'fr-ca';
      break;
    default:
      momentLanguage = 'en';
  }

  moment.updateLocale(momentLanguage, {
    week: {
      dow: 1,
    },
  });

  moment.tz.setDefault(moment.tz.guess(true));
  moment.locale(momentLanguage);

  return moment;
};

export default localizedMoment;
