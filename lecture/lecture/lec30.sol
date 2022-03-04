// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.0 <0.9.0;

contract lec30{

  modifier onlyAdults{
    revert("You are not allowed to pay for the cigarette");
    _;
  }

  function BuyCigarette() public onlyAdults returns(string memory){
    return "Your payment is succeeded";
  }

  modifier onlyAdults2(uint _age){
    require(_age>18,"You are not allowed to pay for the cigarette");
    _;
  }

  function BuyCigarette2(uint _age) public onlyAdults2(_age) returns(string memory){
    return "Your payment is succeeded";
  }

  uint256 public num = 5;
  modifier numChnage{
    num = 10;
    _;
  }

  function numChangeFunction() public numChnage{
    num = 15;
  } // 결과 num = 15
}