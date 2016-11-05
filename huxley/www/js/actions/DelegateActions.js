/**
 * Copyright (c) 2011-2016 Berkeley Model United Nations. All rights reserved.
 * Use of this source code is governed by a BSD License (see LICENSE).
 */

'use strict';

var ActionConstants = require('constants/ActionConstants');
var Dispatcher = require('dispatcher/Dispatcher');

var DelegateActions = {
  deleteDelegate(delegate) {
    Dispatcher.dispatch({
      actionType: ActionConstants.DELETE_DELEGATE,
      delegate: delegate
    });
  },

  addDelegate(delegate) {
    Dispatcher.dispatch({
      actionType: ActionConstants.ADD_DELEGATE,
      delegate: delegate
    });
  },

  updateDelegate(delegateID, name, email, schoolID) {
    Dispatcher.dispatch({
      actionType: ActionConstants.UPDATE_DELEGATE,
      delegateID: delegateID,
      name: name,
      email: email,
      schoolID: schoolID
    });
  }
};

module.exports = DelegateActions;
