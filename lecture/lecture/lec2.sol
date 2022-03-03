// SPDX-License-Identifier GPL-30

pragma solidity >= 0.7.0 < 0.9.0;

contract lec2{
    
    //boolean : true /false
    bool public b = false;

    // ! || == &&
    bool public b1 = !false; // true
    bool public b2 = false || true; // true
    bool public b3 = false == true; // false
    bool public b4 = false && true; // false

    // bytes 1 ~ 32
    bytes4 public bt = 0x12345678;
    bytes public bt2 = "STRING"; // 스트링이 바이트화 되어서 변환

    //address : 이더 송수신시 어드레스 통하여 주고받음, 스마트 컨트랙마다 배포가되면 
    //address가 생김
    address public addr = 0xd8b934580fcE35a11B58C6D73aDeE468a2833fa8;

    //int vs uint : 마이너스가 있냐 없냐
    
    //int8
    // -2^7 ~ 2^7 - 1

    //uint8
    // 0 ~ 2^8 - 1
    int8 public it = 4;

    //uint8
    // 0 ~ 2^8-1
    uint256 public uit = 132213;
    // + - = /

    
}