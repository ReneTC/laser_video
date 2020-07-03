import skia
import glfw
from OpenGL import GL
import time
import random

width, height = 200, 200

def init_surface(width, height):
    context = skia.GrContext.MakeGL()
    backend_render_target = skia.GrBackendRenderTarget(
        width,
        height,
        0,  # sample count
        0,  # stencil bits
        skia.GrGLFramebufferInfo(0, GL.GL_RGBA8))
    surface = skia.Surface.MakeFromBackendRenderTarget(
        context, backend_render_target, skia.kBottomLeft_GrSurfaceOrigin,
        skia.kRGBA_8888_ColorType, skia.ColorSpace.MakeSRGB())
    assert surface, 'Failed to create a surface'
    return surface

if not glfw.init():
    raise RuntimeError('glfw.init() failed')

glfw.window_hint(glfw.STENCIL_BITS, 0)
glfw.window_hint(glfw.DEPTH_BITS, 0)

window = glfw.create_window(640, 480, 'Demo', None, None)
glfw.make_context_current(window)
glfw.swap_interval(1)

surface = init_surface(width, height)
canvas = surface.getCanvas()

frameRate = 60
elapsedTime = time.perf_counter()

# Loop until the user closes the window
while not glfw.window_should_close(window):
    #glfw.wait_events()

    # calculate frame rate
    frameRate = round(1/(time.perf_counter() - elapsedTime), 2)
    elapsedTime = time.perf_counter()
    print(frameRate)

    # Render here
    canvas.clear(skia.ColorGREEN)

    paint = skia.Paint()
    paint.setAntiAlias(True)
    paint.setStyle(skia.Paint.kStroke_Style)
    paint.setStrokeWidth(8)
    paint.setStrokeCap(skia.Paint.kRound_Cap)

    s = 50
    for x in range(s):
        for y in range(s):
            px, py = (random.randint(0, width), random.randint(0, height))
            path = skia.Path()
            path.moveTo(px, py)
            path.lineTo(px, py)
            canvas.drawPath(path, paint)

    surface.flushAndSubmit()

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

glfw.terminate()
