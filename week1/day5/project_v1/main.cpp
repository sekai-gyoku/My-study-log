#include <iostream>
#include <string>
#include "message.h"


int main(int argc,char* argv[]){
    std::string user_name = "default_user";

    if (argc >=2){
        user_name = argv[1];
    }

    std::cout << "Day 5: start C++ basics" << std::endl;
    std::cout << build_message() << std::endl;
    std::cout << build_target_name() << std::endl;
    std::cout << "User: "<< user_name << std::endl;
    
    return 0;
}