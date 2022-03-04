// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.0 <0.9.0;

contract lec29{
  function add(uint256 _num1, uint256 _num2) public pure returns (uint256){
    uint256 total = _num1 + _num2;
    return total;
  }

  function add2(uint256 _num1, uint256 _num2) public pure returns (uint256 total){
    total = _num1 + _num2;
    return total;
  }
}