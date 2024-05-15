import 'bootstrap' // load bootstrap components
import 'django'
import 'select2' // used to skin select element used in livequestions
import 'slick-carousel' // for project timeline

import '../../../apps/actions/assets/timestamps.js'
import '../../../apps/dashboard/assets/ajax_modal.js'
import '../../../apps/maps/assets/map-address.js'
import '../../../apps/moderatorremark/assets/idea_remarks.js'
import '../../../apps/newsletters/assets/dynamic_fields.js'

// expose react components
import {
  commentsAsync as ReactCommentsAsync,
  follows as ReactFollows,
  ratings as ReactRatings,
  reports as ReactReports,
  widget as ReactWidget
} from 'adhocracy4'

import { init as renderChoins } from '../../../apps/fairvote/assets/choins/react_choins_init.jsx'
import { init as renderUserIdeaChoins } from '../../../apps/fairvote/assets/choins/react_user_idea_choins_init.jsx'
import { init as renderInvestedChoins } from '../../../apps/fairvote/assets/choins/react_invested_choins_init.jsx'
import { init as renderRatingChoins } from '../../../apps/fairvote/assets/ratings/react_ratings_init.jsx'

import { renderLanguageChoice } from '../../../apps/organisations/assets/react_language_choice.jsx'

function init () {
  ReactWidget.initialise('a4', 'comment_async', ReactCommentsAsync.renderComment)
  ReactWidget.initialise('a4', 'follows', ReactFollows.renderFollow)
  ReactWidget.initialise('a4', 'ratings', ReactRatings.renderRatings)
  ReactWidget.initialise('a4', 'reports', ReactReports.renderReports)

  ReactWidget.initialise('aplus', 'ratings', renderRatingChoins)

  ReactWidget.initialise('euth', 'language-choice', renderLanguageChoice)
  ReactWidget.initialise('aplus', 'choins', renderChoins)
  ReactWidget.initialise('aplus', 'fv_modules', renderUserIdeaChoins)
  ReactWidget.initialise('aplus', 'invested_choins', renderInvestedChoins)

  $('.timeline-carousel__item').slick({
    initialSlide: parseInt($('#timeline-carousel').attr('data-initial-slide')),
    focusOnSelect: false,
    centerMode: true,
    dots: false,
    arrows: true,
    centerPadding: 30,
    mobileFirst: true,
    infinite: false,
    variableWidth: true,
    slidesToShow: 1,
    slidesToScroll: 1
  })

  $('.project-tile-carousel').slick({
    initialSlide: 0,
    focusOnSelect: false,
    centerMode: false,
    dots: false,
    arrows: false,
    centerPadding: 30,
    mobileFirst: true,
    infinite: false,
    variableWidth: false,
    slidesToShow: 1.2,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          arrows: true
        }
      }
    ]
  })

  if ($.fn.select2) {
    $('.js-select2').select2()
  }
}

document.addEventListener('DOMContentLoaded', init, false)

export function getCurrentPath () {
  return location.pathname
}
