// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FoodTraceability {

    struct Product {
        uint256 id;
        string name;
        string origin;
        address currentOwner;
        string status;
        uint256 timestamp;
    }

    uint256 public productCount = 0;

    mapping(uint256 => Product) public products;

    event ProductRegistered(
            uint256 id,
            string name,
            string origin,
            address owner,
            uint timestamp
        );   

    function registerProduct(
        string memory _name,
        string memory _origin
    ) public {

        productCount++;

        products[productCount] = Product(
            productCount,
            _name,
            _origin,
            msg.sender,
            "Registered",
            block.timestamp
        );

        emit ProductRegistered(
            productCount,
            _name,
            _origin,
            msg.sender,
            block.timestamp
        );
    }

}

    
