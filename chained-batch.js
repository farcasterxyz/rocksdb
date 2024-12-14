'use strict'

/**
 * This module implements the ChainedBatch class, which extends AbstractChainedBatch 
 * from the abstract-leveldown library.
 * 
 * ChainedBatch is used to create a chain of batch operations for interacting with 
 * a LevelDB-like database. This implementation performs operations through native 
 * bindings, allowing efficient execution of database operations without calling 
 * each one separately.
 * 
 * The primary purpose of this class is to group multiple operations into one 
 * atomic batch, improving performance.
 */

const util = require('util')
const AbstractChainedBatch = require('abstract-leveldown').AbstractChainedBatch
const binding = require('./binding')

/**
 * Constructor for ChainedBatch.
 * Initializes the object that inherits from AbstractChainedBatch and creates 
 * a context for performing batch operations using native bindings.
 * 
 * @param {Object} db - The database instance on which operations will be performed.
 */
function ChainedBatch (db) {
  // Call the constructor of the parent class AbstractChainedBatch
  AbstractChainedBatch.call(this, db)
  
  // Initialize the batch operation context using the binding module
  this.context = binding.batch_init(db.context)
}

/**
 * Method to add a "put" operation to the batch.
 * 
 * @param {Buffer|string} key - The key where the data will be stored.
 * @param {Buffer|string} value - The value to be stored.
 */
ChainedBatch.prototype._put = function (key, value) {
  // Add the "put" operation to the batch
  binding.batch_put(this.context, key, value)
}

/**
 * Method to add a "del" operation to the batch (delete data).
 * 
 * @param {Buffer|string} key - The key for the data to be deleted.
 */
ChainedBatch.prototype._del = function (key) {
  // Add the "del" operation to the batch (delete the data)
  binding.batch_del(this.context, key)
}

/**
 * Method to clear all operations in the batch.
 * This removes all "put" and "del" operations added to the batch.
 */
ChainedBatch.prototype._clear = function () {
  // Clear all operations from the batch
  binding.batch_clear(this.context)
}

/**
 * Method to write all operations in the batch to the database.
 * After this method is called, all the batch operations are executed and persisted.
 * 
 * @param {Object} options - Options for the write operation.
 * @param {function} callback - A callback function that will be called after the write operation completes.
 */
ChainedBatch.prototype._write = function (options, callback) {
  // Execute all batch operations and write them to the database
  binding.batch_write(this.context, options, callback)
}

// Set up inheritance from AbstractChainedBatch
util.inherits(ChainedBatch, AbstractChainedBatch)

// Export the ChainedBatch module to be used in other parts of the application
module.exports = ChainedBatch
