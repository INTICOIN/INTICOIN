/**
* @file       INTICOINX.h
*
* @brief      Exceptions and constants for INTICOINX
*
* @author     Ian Miers, Christina Garman and Matthew Green
* @date       June 2013
*
* @copyright  Copyright 2013 Ian Miers, Christina Garman and Matthew Green
* @license    This project is released under the MIT license.
**/

#ifndef INTICOINX_H_
#define INTICOINX_H_

#include <stdexcept>

#define INTICOINX_DEFAULT_SECURITYLEVEL      80
#define INTICOINX_MIN_SECURITY_LEVEL         80
#define INTICOINX_MAX_SECURITY_LEVEL         80
#define ACCPROOF_KPRIME                     160
#define ACCPROOF_KDPRIME                    128
#define MAX_COINMINT_ATTEMPTS               10000
#define INTICOINX_MINT_PRIME_PARAM           20
#define INTICOINX_VERSION_STRING             "0.11"
#define INTICOINX_VERSION_INT                11
#define INTICOINX_PROTOCOL_VERSION           "1"
#define HASH_OUTPUT_BITS                    256
#define INTICOINX_COMMITMENT_EQUALITY_PROOF  "COMMITMENT_EQUALITY_PROOF"
#define INTICOINX_ACCUMULATOR_PROOF          "ACCUMULATOR_PROOF"
#define INTICOINX_SERIALNUMBER_PROOF         "SERIALNUMBER_PROOF"

// Activate multithreaded mode for proof verification

//#define INTICOINX_THREADING 1

// Uses a fast technique for coin generation. Could be more vulnerable
// to timing attacks. Turn off if an attacker can measure coin minting time.
#define INTICOINX_FAST_MINT 1

// Errors thrown by the INTICOINX library

class INTICOINXException : public std::runtime_error
{
public:
   explicit INTICOINXException(const std::string& str) : std::runtime_error(str) {}
};

#include "../serialize.h"
#include "../bignum.h"
#include "../util.h"
#include "Params.h"
#include "Coin.h"
#include "Commitment.h"
#include "Accumulator.h"
#include "AccumulatorProofOfKnowledge.h"
#include "CoinSpend.h"
#include "SerialNumberSignatureOfKnowledge.h"
#include "ParamGeneration.h"

#endif /* INTICOINX_H_ */
