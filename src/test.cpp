#include "murmur3.h"
#include <iostream>

int main(int argc, char **argv)
{
    auto hash = yamh::murmur3_32();

    if (argc == 1)
    {
        std::cout << "No arguments passed, requires 1 argument" << std::endl;
        return 1;
    }

    hash.update(argv[1]);
    std::cout << "Digest: " << hash.digest() << std::endl;
    return 0;
}
