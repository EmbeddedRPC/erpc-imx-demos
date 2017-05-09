/*
 * Generated by erpcgen 1.4.0 on Tue May  9 14:15:01 2017.
 *
 * AUTOGENERATED - DO NOT EDIT
 */

#include "erpc_matrix_multiply.h"
#include "client_manager.h"
#include "erpc_port.h"

using namespace erpc;
#if !(__embedded_cplusplus)
using namespace std;
#endif

extern ClientManager *g_client;

// Constant variable definitions
const int32_t matrix_size = 5;


// MatrixMultiplyService interface erpcMatrixMultiply function client shim.
void erpcMatrixMultiply(const Matrix * matrix1, const Matrix * matrix2, Matrix * result_matrix)
{
    erpc_status_t err = kErpcStatus_Success;

    // Get a new request.
    RequestContext request = g_client->createRequest(false);

    // Encode the request.
    Codec * codec = request.getCodec();
    if (codec == NULL)
    {
        err = kErpcStatus_MemoryError;
    }

    if (!err)
    {
        err = codec->startWriteMessage(kInvocationMessage, kMatrixMultiplyService_service_id, kMatrixMultiplyService_erpcMatrixMultiply_id, request.getSequence());
    }
    if (!err)
    {
        for (uint32_t arrayCount1 = 0; arrayCount1 < 5; ++arrayCount1)
        {
            for (uint32_t arrayCount2 = 0; arrayCount2 < 5; ++arrayCount2)
            {
                if (!err)
                {
                    err = codec->write((*matrix1)[arrayCount1][arrayCount2]);
                }
                else
                {
                    break;
                }
            }
        }
    }

    if (!err)
    {
        for (uint32_t arrayCount1 = 0; arrayCount1 < 5; ++arrayCount1)
        {
            for (uint32_t arrayCount2 = 0; arrayCount2 < 5; ++arrayCount2)
            {
                if (!err)
                {
                    err = codec->write((*matrix2)[arrayCount1][arrayCount2]);
                }
                else
                {
                    break;
                }
            }
        }
    }

    if (!err)
    {
        err = codec->endWriteMessage();
    }

    // Send message to server
    if (!err)
    {
        err = g_client->performRequest(request);
    }

    if (!err)
    {
        for (uint32_t arrayCount1 = 0; arrayCount1 < 5; ++arrayCount1)
        {
            for (uint32_t arrayCount2 = 0; arrayCount2 < 5; ++arrayCount2)
            {
                if (!err)
                {
                    err = codec->read(&(*result_matrix)[arrayCount1][arrayCount2]);
                }
                else
                {
                    break;
                }
            }
        }
    }

    if (!err)
    {
        err = codec->endReadMessage();
    }

    // Dispose of the request.
    g_client->releaseRequest(request);

    if (err)
    {
        client_error_handler_t errorHandler = g_client->getErrorHandler();
        if (errorHandler != NULL)
        {
            (*errorHandler)(err);
        }
        
    }

    return;
}
