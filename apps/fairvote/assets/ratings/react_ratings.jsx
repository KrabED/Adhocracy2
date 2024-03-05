import React from 'react'
import django from 'django'

import Api from '../api'
import { RatingBox } from 'adhocracy4/adhocracy4/ratings/static/ratings/react_ratings'
const translations = {
  upvote: django.gettext('vote')
}

export default class RatingChoinsBox extends RatingBox {
  handleRatingCreate (number) {
    super.handleRatingCreate(number)
    console.log(this.props.objectId)
    Api.rating.add({
      value: number,
      ideaId: this.props.objectId
    })
      .then((response) => {
        console.log('Success:', response)
      })
      .catch((error) => {
        alert('An error occurred. Please try again: ', error.JSONResponse.message)
        console.log('Error Details:', error)
      })
  }

  handleRatingModify (number, id) {
    const oldValue = this.state.userRating
    console.log(this.props.objectId)

    super.handleRatingModify(number, id)
    Api.rating.change({
      oldValue,
      newValue: number,
      ideaId: this.props.objectId
    })
      .then((response) => {
        console.log('Success:', response)
      })
      .catch((error) => {
        alert('An error occurred. Please try again.' + error.responseJSON.message)
        console.log('Error Details:', error.responseJSON.message)
      })
  }

  render () {
    const getRatingClasses = ratingType => {
      const valueForRatingType = ratingType === 'up' ? 1 : -1
      const disabled = this.props.idea_status === 'ACCEPTED' ? 'disabled' : ''
      const cssClasses = this.state.userRating === valueForRatingType
        ? 'rating-button rating-' + ratingType + ' is-selected' + disabled
        : 'rating-button rating-' + ratingType + disabled
      return cssClasses
    }

    return (
      <div className="rating">
        <button
          name="upvote"
          aria-label={translations.upvote}
          className={getRatingClasses('up')}
          disabled={this.props.isReadOnly}
          onClick={this.ratingUp.bind(this)}
        >
          <i className="fa fa-chevron-up" aria-hidden="true" />
          {translations.upvote}
        </button>
        <i className="fas fa-user" aria-hidden="true" />
        {this.state.positiveRatings}
      </div>
    )
  }
}
