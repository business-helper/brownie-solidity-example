// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    // uint256 favoriteNumber = 5;
    // bool favoriteBool = true;
    // string favoriteString = "String";
    // int256 favoriteInt = -5;
    // address favoriteAddress = 0x0A92DD7B30f0f57343AD99a151dBC37a3F3F95F3;
    // bytes32 favoriteBytes = "cat";

    uint256 favoriteNumber;
    bool favoriteBool;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    People public person = People({favoriteNumber: 2, name: "Martin"});

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
        // uint256 test = 4;
    }

    // function store2() public {

    // }

    // pure function performs math operations only
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        // people.push(People({ favoriteNumber: _favoriteNumber, name: _name }));
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
