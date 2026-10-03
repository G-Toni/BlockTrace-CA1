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
        uint256 timestamp
    );

    event ProductTransferred(
        uint256 id,
        address previousOwner,
        address newOwner,
        uint256 timestamp
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

    function transferProduct(
        uint256 _id,
        address _newOwner
    ) public {

        require(
            _id > 0 && _id <= productCount,
            "Product does not exist"
        );

        Product storage product = products[_id];

        require(
            msg.sender == product.currentOwner,
            "Only current owner can transfer product"
        );

        require(
            _newOwner != address(0),
            "Invalid receiver address"
        );

        address previousOwner = product.currentOwner;

        product.currentOwner = _newOwner;

        emit ProductTransferred(
            _id,
            previousOwner,
            _newOwner,
            block.timestamp
        );
    }
}
