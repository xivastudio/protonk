#To enable these settings, name this file "user_settings.py".

#Settings here will take effect for all games run in this Proton version.

user_settings = {

    #Enable integer scaling mode
    "WINE_FULLSCREEN_INTEGER_SCALING": "1",

    #Enable DXVK async patch
    "DXVK_ASYNC": "1",

    #Enable DXVK State Cache
    "DXVK_STATE_CACHE": "1",

    #Enable LatencyFleX
    "LFX": "1",

    #Disable nvapi and nvapi64
    "PROTON_NVAPI_DISABLE": "1",

    #Disable winedbg
    "PROTON_WINEDBG_DISABLE": "1",

    #Reduce Pulse Latency
    "PROTON_PULSE_LOWLATENCY": "1",

    #Spoof d3d12 feature level supported by vkd3d. Needed for some d3d12 games to work.
    "VKD3D_FEATURE_LEVEL": "12_0",

    #Enable Vulkan/OpenGL game capture
    "OBS_VKCAPTURE": "1",

    #By default, logs are saved to $HOME/steam-<STEAM_GAME_ID>.log, overwriting any previous log with that name.
    #Log directory can be overridden with $PROTON_LOG_DIR.

    #Wine debug logging
#    "WINEDEBUG": "+timestamp,+pid,+seh,+unwind,+debugstr,+loaddll,+mscoree",

    #DXVK debug logging
#    "DXVK_LOG_LEVEL": "info",

    #vkd3d debug logging
#    "VKD3D_DEBUG": "warn",

    #vkd3d-shader debug logging
#    "VKD3D_SHADER_DEBUG": "fixme",

    #wine-mono debug logging (Wine's .NET replacement)
#    "WINE_MONO_TRACE": "E:System.NotImplementedException",
    #"MONO_LOG_LEVEL": "info",

    #general purpose media logging
#    "GST_DEBUG": "4",
    #or, verbose converter logging (may impact playback performance):
#    "GST_DEBUG": "4,WINE:7,protonaudioconverter:7,protonaudioconverterbin:7,protonvideoconverter:7",
#    "GST_DEBUG_NO_COLOR": "1",

    #Enable DXVK's HUD
#    "DXVK_HUD": "devinfo,fps",

    #Use OpenGL-based wined3d for d3d11, d3d10, and d3d9 instead of Vulkan-based DXVK
#    "PROTON_USE_WINED3D": "1",

    #Disable d3d11 entirely
#    "PROTON_NO_D3D11": "1",

    #Disable eventfd-based in-process synchronization primitives
#    "PROTON_NO_ESYNC": "1",

    #Disable futex-based in-process synchronization primitives
#    "PROTON_NO_FSYNC": "1",
}
